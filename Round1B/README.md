
# Adobe Hackathon Round 1B – Intelligent PDF Analyzer

## 🧠 What it Does

- Reads multiple PDFs from `input/`
- Takes `persona.json` to define persona + job
- Ranks most relevant sections
- Outputs final JSON to `output/output.json`

## 🐳 How to Run

### Step 1: Place your files
- Put PDFs in `input/`
- Create `input/persona.json` like:
```json
{
  "persona": "PhD Researcher",
  "job": "Prepare a literature review on GNN methods and benchmarks"
}
```

### Step 2: Build the Docker image
```bash
docker build --platform linux/amd64 -t pdf-intelligent-analyzer:latest .
```

### Step 3: Run the solution
```bash
docker run --rm \
-v $(pwd)/input:/app/input \
-v $(pwd)/output:/app/output \
--network none pdf-intelligent-analyzer:latest
```

✅ Output: `output/output.json`
