import re

def extract_experience(doc):
    """Section-aware extractor that handles ACADEMIC PROJECTS, ADDITIONAL EXPERIENCE, etc."""
    experience = []
    full_text = doc.text
    lines = [l.strip() for l in full_text.split('\n') if l.strip()]

    project_headers = [
        "academic projects", "projects", "personal projects", "key projects",
        "additional experience", "additional experience & certifications", "experience"
    ]
    stop_headers = ["education", "skills", "certifications", "technical skills", "professional summary"]

    current_entries = []
    in_section = False
    current_title = None

    for i, line in enumerate(lines):
        lower = line.lower()

        # Detect section start
        if any(h in lower for h in project_headers) and not in_section:
            in_section = True
            continue

        if in_section:
            if any(h in lower for h in stop_headers):
                break

            # Treat lines that look like project/role titles (often Title then description)
            # Simple heuristic: short lines followed by longer descriptive text are titles
            is_title_like = (
                len(line) < 90 and
                not line.startswith("•") and
                not re.match(r'^\d', line) and
                not any(x in lower for x in ["designed", "utilized", "developed", "conducted", "optimized", "generated"])
            )

            if is_title_like and len(line.split()) > 1:
                if current_entries:
                    experience.append(current_entries[0])
                current_entries = [{"description": line, "company": None, "duration": None, "title": line}]
            elif current_entries:
                # append to last entry's description
                last = current_entries[0]
                if len(line) > 10:
                    combined = (last.get("description", "") + " " + line).strip()
                    last["description"] = combined[:350]
            else:
                # standalone bullet or sentence
                clean = line.replace("•", "").strip()
                if len(clean) > 15:
                    experience.append({
                        "description": clean[:320],
                        "company": None,
                        "duration": None
                    })

    # flush last
    if current_entries:
        experience.append(current_entries[0])

    # Final cleanup + dedup
    cleaned = []
    seen = set()
    for e in experience:
        desc = e.get("description", "").strip()
        if len(desc) < 12:
            continue
        key = desc[:60].lower()
        if key in seen:
            continue
        seen.add(key)
        cleaned.append({
            "description": desc,
            "company": e.get("company"),
            "duration": e.get("duration")
        })

    return cleaned[:6]  # limit noise