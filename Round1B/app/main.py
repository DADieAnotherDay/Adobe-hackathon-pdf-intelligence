
import os
import json
from datetime import datetime
from utils import extract_sections, rank_sections, summarize_text

INPUT_DIR = "/app/input"
OUTPUT_DIR = "/app/output"
META_FILE = "/app/input/persona.json"

def main():
    with open(META_FILE, "r", encoding="utf-8") as f:
        metadata = json.load(f)

    all_sections = []
    all_subsections = []

    for filename in os.listdir(INPUT_DIR):
        if filename.lower().endswith(".pdf"):
            filepath = os.path.join(INPUT_DIR, filename)
            sections = extract_sections(filepath)
            ranked = rank_sections(sections, metadata["job"])
            for r in ranked:
                all_sections.append({
                    "document": filename,
                    "page": r["page"],
                    "section_title": r["title"],
                    "importance_rank": r["rank"]
                })
                all_subsections.append({
                    "document": filename,
                    "page": r["page"],
                    "refined_text": summarize_text(r["content"])
                })

    output = {
        "metadata": {
            "documents": [f for f in os.listdir(INPUT_DIR) if f.endswith(".pdf")],
            "persona": metadata["persona"],
            "job": metadata["job"],
            "timestamp": datetime.now().isoformat()
        },
        "sections": all_sections,
        "subsections": all_subsections
    }

    with open(os.path.join(OUTPUT_DIR, "output.json"), "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()
