
import fitz
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_sections(pdf_path):
    doc = fitz.open(pdf_path)
    sections = []
    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("blocks")
        for block in blocks:
            text = block[4].strip()
            if len(text.split()) > 5:
                sections.append({
                    "title": text.split("\n")[0],
                    "content": text,
                    "page": page_num
                })
    return sections

def rank_sections(sections, job_text):
    texts = [s["content"] for s in sections]
    tfidf = TfidfVectorizer(stop_words="english").fit_transform([job_text] + texts)
    similarities = cosine_similarity(tfidf[0:1], tfidf[1:]).flatten()
    ranked = sorted(
        [{"score": sim, **sec} for sim, sec in zip(similarities, sections)],
        key=lambda x: x["score"], reverse=True
    )
    for i, r in enumerate(ranked[:5]):
        r["rank"] = i + 1
    return ranked[:5]

def summarize_text(text):
    sentences = text.split(". ")
    return ". ".join(sentences[:2]) + ("..." if len(sentences) > 2 else "")
