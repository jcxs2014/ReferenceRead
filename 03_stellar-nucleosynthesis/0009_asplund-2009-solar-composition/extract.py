import fitz, os, json
base = "/Users/jcxs2014/Sites/HermesLocal/papers/03_stellar-nucleosynthesis/0009_asplund-2009-solar-composition"
out = "/Users/jcxs2014/Sites/HermesLocal/papers/03_stellar-nucleosynthesis/0009_asplund-2009-solar-composition/extracted"
os.makedirs(out, exist_ok=True)
for f in sorted(os.listdir(base)):
    if not f.endswith(".pdf"): continue
    doc = fitz.open(os.path.join(base, f))
    fn = f.replace(" ", "_").replace(".pdf", "")
    pages = []
    for i, page in enumerate(doc):
        txt = page.get_text()
        pages.append({"page": i+1, "text": txt})
    with open(os.path.join(out, fn + ".json"), "w", encoding="utf-8") as fh:
        json.dump(pages, fh, ensure_ascii=False, indent=1)
    total_chars = sum(len(p["text"]) for p in pages)
    print(f, "pages:", len(doc), "chars:", total_chars)
