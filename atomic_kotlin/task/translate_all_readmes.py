import os
import json
import urllib.request
import re
import time

TEXT_FILE = "/tmp/Atomic_Kotlin.txt"
BASE_DIR = "/Users/keke/Documents/GitHub/code-index/atomic_kotlin/Examples"
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "exaone3.5:latest"

def camel_case_split(identifier):
    # 'VarAndVal' -> 'Var And Val'
    matches = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', identifier)
    words = [m.group(0) for m in matches]
    
    # 특수 케이스 처리 (예: And -> &, HelloWorld -> Hello, World!)
    text = " ".join(words)
    text = text.replace("And", "&")
    if text == "Hello World":
        text = "Hello, World!"
    # 등등 대략적인 변환
    return text

def get_chapter_text_from_pdf(folder_name, full_text):
    # 폴더명 분석: '04_VarAndVal' -> 'VarAndVal'
    parts = folder_name.split("_", 1)
    if len(parts) < 2: return ""
    
    chapter_topic = camel_case_split(parts[1])
    
    # 본문 텍스트 (앞부분 목차 스킵)
    body_text = "\n".join(full_text.split("\n")[800:])
    
    # 챕터 제목으로 대략적인 위치 검색 (대소문자 무시)
    pattern = re.compile(rf"^\s*{re.escape(chapter_topic)}\s*$", re.IGNORECASE | re.MULTILINE)
    match = pattern.search(body_text)
    
    if match:
        start_idx = match.end()
        # 챕터 내용을 적당히 4000자 정도 추출 (다음 챕터까지 찾기 복잡할 수 있으므로)
        extracted = body_text[start_idx:start_idx+4000]
        return extracted
    
    return ""

def call_llm(prompt_text):
    data = {
        "model": MODEL_NAME,
        "prompt": prompt_text,
        "stream": False
    }
    
    req = urllib.request.Request(OLLAMA_URL, data=json.dumps(data).encode("utf-8"), headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode())
            return result.get("response", "").strip()
    except Exception as e:
        print(f"LLM API Error: {e}")
        return ""

def process_all_chapters():
    with open(TEXT_FILE, "r", encoding="utf-8") as f:
        full_text = f.read()

    folders = sorted([f for f in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, f)) and f[0].isdigit()])
    
    # 이미 처리된 앞 챕터는 스킵
    skip_list = ["03_HelloWorld", "04_VarAndVal"]

    for folder in folders:
        if folder in skip_list:
            continue
            
        print(f"Processing {folder}...")
        
        # PDF에서 텍스트 추출 시도
        extracted_text = get_chapter_text_from_pdf(folder, full_text)
        
        chapter_num = folder.split('_')[0]
        chapter_name = folder.split('_')[1] if len(folder.split('_')) > 1 else folder
        
        # 텍스트 추출 실패시 LLM 자체 지식 활용하도록 유도
        if extracted_text:
            context = f"[원문 참고 텍스트]\n{extracted_text}"
        else:
            context = f"(PDF 본문 매칭 실패 - Atomic Kotlin 책의 '{chapter_name}' 내용에 기반하여 작성해주세요)"

        prompt = f"""당신은 코틀린 프로그래밍을 처음 배우는 사람들을 위해 친절하게 설명하는 강사입니다.
Atomic Kotlin 책의 챕터 '{folder}' 주제에 대해 마크다운(Markdown) 형식의 README.md 내용을 한국어로 작성해주세요.

다음 제공되는 책의 원문 텍스트를 반드시 바탕으로, 초보자가 이해하기 쉽도록 풀어서 설명해주세요:

{context}

[요청 사항]
1. 문서의 시작은 `# {chapter_num}. {chapter_name}` 와 같이 제목으로 시작해주세요.
2. 예제 코드가 있다면 코드 블록으로 작성해서 보여주세요.
3. 초보자의 눈높이에 맞춰 친근한 말투(해요체 등)를 사용해주세요.
4. 주요 핵심 개념을 요약해서 알려주세요.
        """

        kor_summary = call_llm(prompt)
        
        if kor_summary:
            readme_path = os.path.join(BASE_DIR, folder, "README.md")
            with open(readme_path, "w", encoding="utf-8") as rf:
                rf.write(kor_summary)
            print(f"[{folder}] README.md 작성 완료!")
        else:
            print(f"[{folder}] LLM 응답 실패")
            
        # 연속 호출 시 LLM 서버 부하 방지
        time.sleep(2)

if __name__ == "__main__":
    print("전체 README 번역 프로세스 시작...")
    process_all_chapters()
    print("모든 처리 완료!")
