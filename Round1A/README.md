
# Adobe Hackathon Round 1A – PDF Outline Extractor

## 🔧 How It Works

This solution extracts:
- Title
- Headings (H1, H2, H3)
- Page numbers

Using PyMuPDF for layout + font size-based detection.

## 🐳 Docker Instructions

### Build:
```bash
docker build --platform linux/amd64 -t pdf-outline-extractor:latest .
```

### Run:
```bash
docker run --rm \
-v $(pwd)/input:/app/input \
-v $(pwd)/output:/app/output \
--network none pdf-outline-extractor:latest
```

## 🧠 Notes:
- Font size is used to detect heading levels
- No internet or external dependencies
