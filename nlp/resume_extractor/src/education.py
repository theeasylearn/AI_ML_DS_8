import re

def extract_education(doc):
    """Robust education extraction using header context + patterns."""
    education = []
    full_text = doc.text
    lines = [l.strip() for l in full_text.split('\n') if l.strip()]

    # Find EDUCATION section
    edu_section_lines = []
    in_edu = False
    edu_headers = ['education', 'academic background', 'educational qualifications']

    for i, line in enumerate(lines):
        lower = line.lower()
        if any(h in lower for h in edu_headers):
            in_edu = True
            continue
        if in_edu:
            # Stop at next major section
            if any(h in lower for h in ['additional experience', 'certification', 'experience', 'skills', 'projects', 'summary']):
                break
            edu_section_lines.append(line)

    # Also scan whole doc for strong degree patterns as fallback
    candidates = edu_section_lines or lines

    for line in candidates:
        lower = line.lower()

        # Look for degree + college indicators
        degree_indicators = ['b.tech', 'bachelor', 'b.e', 'master', 'm.tech', 'msc', 'bca', 'mca']
        if not any(d in lower for d in degree_indicators):
            continue

        year = re.search(r'(20\d{2}|19\d{2})', line) or re.search(r'Graduation Year:\s*(\d{4})', line, re.I)
        year_val = year.group(1) if year and year.lastindex else (year.group() if year else None)

        # GPA / percentage / CGPA
        gpa_match = re.search(r'(?:GPA|CGPA|Cumulative GPA)[:\s]*([\d.]+)\s*/\s*([\d.]+)', line, re.I)
        pct_match = re.search(r'([\d.]+)\s*/\s*10\.0|(\d{1,2}(?:\.\d{1,2})?)\s*%', line, re.I)

        score = None
        if gpa_match:
            score = f"{gpa_match.group(1)}/{gpa_match.group(2)}"
        elif pct_match:
            score = pct_match.group(0)

        # Clean
        clean = re.sub(r'\s+', ' ', line).strip()
        if len(clean) > 250:
            clean = clean[:247] + "..."

        # Try to separate degree and institution
        inst_match = re.search(r'(?:in|–|-)\s*([^—]+?)(?:\s*—|\s*,|\s*Graduation)', clean, re.I)
        institution = inst_match.group(1).strip() if inst_match else None

        entry = {
            "degree": clean,
            "year": year_val,
            "percentage": score,
        }
        if institution:
            entry["institution"] = institution

        # Avoid adding junk
        if 'technical localization' not in clean.lower() and len(clean) > 15:
            # dedup
            if not any(e.get('degree', '')[:40] == clean[:40] for e in education):
                education.append(entry)

    return education