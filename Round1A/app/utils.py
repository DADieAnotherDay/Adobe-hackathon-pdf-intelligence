
import fitz

def extract_outline(pdf_path):
    doc = fitz.open(pdf_path)
    font_sizes = []

    content = []

    # Collect font sizes
    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    font_sizes.append(span["size"])

    # Sort and pick top 3 unique font sizes (used for H1, H2, H3)
    sizes = sorted(list(set(font_sizes)), reverse=True)
    h1_size = sizes[0] if len(sizes) > 0 else None
    h2_size = sizes[1] if len(sizes) > 1 else None
    h3_size = sizes[2] if len(sizes) > 2 else None

    title = ""
    outline = []

    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    text = span["text"].strip()
                    if not text:
                        continue

                    size = span["size"]

                    if not title and size == h1_size:
                        title = text

                    if size == h1_size:
                        outline.append({"level": "H1", "text": text, "page": page_num})
                    elif size == h2_size:
                        outline.append({"level": "H2", "text": text, "page": page_num})
                    elif size == h3_size:
                        outline.append({"level": "H3", "text": text, "page": page_num})

    return {
        "title": title or "Untitled Document",
        "outline": outline
    }
