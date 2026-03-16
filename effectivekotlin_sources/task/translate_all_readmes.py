import os
import json
import urllib.request
import re
import time

TEXT_FILE = "/tmp/Effective_Kotlin.txt"
# Effective Kotlin snippets directory
BASE_DIR = "/Users/keke/Documents/GitHub/code-index/effectivekotlin_sources/src/main/kotlin/snippets"
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "gemma3:27b-cloud"

def extract_item_number(folder_name):
    # 'C1_Item01' -> '1'
    # 'C2_Item10' -> '10'
    match = re.search(r'Item(\d+)', folder_name)
    if match:
        return str(int(match.group(1)))
    return None

def get_item_text_from_pdf(folder_name, full_text):
    item_num = extract_item_number(folder_name)
    if not item_num:
        return ""
    
    # Search for "Item X: Title"
    # Using a simpler pattern as seen in grep results: "Item 1: Limit mutability"
    pattern_start = re.compile(rf"^\s*Item {item_num}:", re.IGNORECASE | re.MULTILINE)
    next_item_num = str(int(item_num) + 1)
    pattern_end = re.compile(rf"^\s*Item {next_item_num}:", re.IGNORECASE | re.MULTILINE)
    
    match_start = pattern_start.search(full_text)
    if not match_start:
        # Try a more flexible pattern if the first one fails
        pattern_start = re.compile(rf"Item {item_num}:", re.IGNORECASE)
        match_start = pattern_start.search(full_text)

    if match_start:
        start_idx = match_start.start()
        match_end = pattern_end.search(full_text, start_idx + 10)
        
        if match_end:
            end_idx = match_end.start()
            extracted = full_text[start_idx:end_idx]
        else:
            # If no next item found, take 5000 chars
            extracted = full_text[start_idx:start_idx+5000]
        
        return extracted.strip()
    
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

def process_all_items():
    if not os.path.exists(TEXT_FILE):
        print(f"Error: {TEXT_FILE} not found. please run pdftotext first.")
        return

    with open(TEXT_FILE, "r", encoding="utf-8") as f:
        full_text = f.read()

    # Get all Item folders, sorted
    folders = sorted([f for f in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, f)) and "Item" in f])
    
    for folder in folders:
        # Check if README.md already exists
        readme_path = os.path.join(BASE_DIR, folder, "README.md")
        if os.path.exists(readme_path):
            # print(f"Skipping {folder}, README.md already exists.")
            continue
            
        print(f"Processing {folder}...")
        
        # Extract original text from PDF dump
        extracted_text = get_item_text_from_pdf(folder, full_text)
        
        item_num = extract_item_number(folder)
        
        if extracted_text:
            context = f"[원문 참고 텍스트]\n{extracted_text}"
        else:
            context = f"(PDF 본문 매칭 실패 - Effective Kotlin 책의 '{folder}' 내용에 기반하여 작성해주세요)"

        prompt = f"""당신은 코틀린 프로그래밍 전문가이자 친절한 강사입니다.
Effective Kotlin 책의 '{folder}' 주제에 대해 마크다운(Markdown) 형식의 README.md 내용을 한국어로 작성해주세요.

다음 제공되는 책의 원문 텍스트를 반드시 바탕으로, 핵심 내용을 잘 정리하고 초보자도 이해하기 쉽게 풀어서 설명해주세요:

{context}

[요청 사항]
1. 문서의 시작은 해당 아이템의 제목(예: # Item 1. 가변성을 제한하라)으로 시작해주세요.
2. 책에서 제시하는 핵심 가이드라인과 그 이유(Best Practice)를 명확히 설명해주세요.
3. 예제 코드가 있다면 코드 블록으로 작성해서 보여주세요. (제공된 텍스트에 코드가 있다면 활용하세요)
4. 친근하고 전문적인 말투(해요체)를 사용해주세요.
5. 문서 마지막에 '핵심 요약' 섹션을 만들어 3~4줄로 정리해주세요.
"""

        kor_summary = call_llm(prompt)
        
        if kor_summary:
            with open(readme_path, "w", encoding="utf-8") as rf:
                rf.write(kor_summary)
            print(f"[{folder}] README.md 작성 완료!")
        else:
            print(f"[{folder}] LLM 응답 실패")
            
        # 연속 호출 시 LLM 서버 부하 방지
        time.sleep(2)

if __name__ == "__main__":
    print("Effective Kotlin README 번역 및 생성 프로세스 시작...")
    process_all_items()
    print("모든 처리 완료!")
