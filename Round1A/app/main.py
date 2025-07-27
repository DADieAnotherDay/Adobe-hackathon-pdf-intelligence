
import os
import json
import fitz  # PyMuPDF
from utils import extract_outline

INPUT_DIR = "/app/input"
OUTPUT_DIR = "/app/output"

def main():
    for filename in os.listdir(INPUT_DIR):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(INPUT_DIR, filename)
            print(f"Processing: {filename}")
            outline_data = extract_outline(pdf_path)

            json_filename = os.path.splitext(filename)[0] + ".json"
            json_path = os.path.join(OUTPUT_DIR, json_filename)

            with open(json_path, "w", encoding="utf-8") as f:
                json.dump(outline_data, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()
