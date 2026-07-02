import re

def extract_certifications(doc):
    """Robust certification extraction."""
    certs = []
    full_text = doc.text
    lines = [l.strip() for l in full_text.split('\n') if l.strip()]

    cert_signals = ["certification", "certified", "certificate", "udemy", "coursera", "nptel"]
    bad_context = ["professional summary", "b.tech", "bachelor of technology", "shantilal", "academic projects", "education"]

    for line in lines:
        lower = line.lower()
        if any(sig in lower for sig in cert_signals):
            if any(bad in lower for bad in bad_context):
                continue
            clean = re.sub(r'\s+', ' ', line.replace('•', '')).strip()
            if len(clean) > 8 and clean not in certs:
                certs.append(clean[:220])

    if not certs:
        matches = re.findall(r'Certification[:\s]*([^\\n(]+?)(?:–|-)\s*([^\\n(]+?)\s*\((\d{4})\)', full_text, re.I)
        for m in matches:
            name = ' - '.join([x.strip() for x in m if x]).strip()
            if name and name not in certs:
                certs.append(name)

    return certs


