import os
import json
import re

TEXT_FILE = "/tmp/Effective_Kotlin.txt"
BASE_DIR = "/Users/keke/Documents/GitHub/code-index/effectivekotlin_sources/src/main/kotlin/snippets"
OUTPUT_FILE = os.path.join(BASE_DIR, "readme_metadata.json")
URL_BASE = "https://raw.githubusercontent.com/cheonkyu/code-index/refs/heads/main/effectivekotlin_sources/src/main/kotlin/snippets"

def extract_item_number(folder_name):
    match = re.search(r'Item(\d+)', folder_name)
    if match:
        return str(int(match.group(1)))
    return None

def find_title_in_text(item_num, full_text):
    # Pattern to find "Item X: Title" or similar
    # In grep results we saw: "35:Item 1: Limit mutability"
    pattern = re.compile(rf"^\s*Item {item_num}:\s*(.*)$", re.IGNORECASE | re.MULTILINE)
    match = pattern.search(full_text)
    if match:
        return f"Item {item_num}. {match.group(1).strip()}"
    
    # Fallback search if the line-start match fails
    pattern_fallback = re.compile(rf"Item {item_num}:\s*(.*)")
    match_fallback = pattern_fallback.search(full_text)
    if match_fallback:
        # Avoid picking up long descriptions, just take the first line or reasonable chunk
        title = match_fallback.group(1).split('\n')[0].strip()
        return f"Item {item_num}. {title}"
        
    return f"Item {item_num}"

def generate_metadata():
    if not os.path.exists(TEXT_FILE):
        print(f"Error: {TEXT_FILE} not found.")
        return

    with open(TEXT_FILE, "r", encoding="utf-8") as f:
        full_text = f.read()

    folders = sorted([f for f in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, f)) and "Item" in f])
    
    metadata = []
    for folder in folders:
        item_num = extract_item_number(folder)
        if not item_num:
            continue
            
        title = find_title_in_text(item_num, full_text)
        url = f"{URL_BASE}/{folder}/README.md"
        
        metadata.append({
            "title": title,
            "url": url
        })
        print(f"Found: {title}")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)
    
    print(f"\nMetadata written to {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_metadata()
