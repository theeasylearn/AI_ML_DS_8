import re

def extract_experience(doc):
    """Section-aware extractor that handles ACADEMIC PROJECTS, ADDITIONAL EXPERIENCE, etc."""
    experience = []
    full_text = doc.text
    lines = [line.strip() for line in full_text.split('\n') if line.strip()]

    project_headers = [
        "academic projects", "projects", "personal projects", "key projects",
        "additional experience", "additional experience & certifications", "experience", "work profile", "portfolio"
    ]

    stop_headers = ["education", "skills", "certifications", "technical skills", "professional summary"]

    current_entries = [] 
    in_section = False 
    for current_line in lines:
        lower = current_line.lower()

        # Detect section start
        if any(header in lower for header in project_headers) and not in_section:
            in_section = True
            continue

        if in_section:
            if any(h in lower for h in stop_headers):
                break

            # Treat lines that look like project/role titles (often Title then description)
            # Simple heuristic: short lines followed by longer descriptive text are titles
            is_title_like = (
                len(current_line) < 90 and not current_line.startswith("•") and not re.match(r'^\d', current_line) and not any(x in lower for x in ["designed", "utilized", "developed", "conducted", "optimized", "generated"])
            )

            if is_title_like and len(current_line.split()) > 1:
                if current_entries:
                    experience.append(current_entries[0])
                current_entries = [{"description": current_line, "company": None, "duration": None, "title": current_line}]
            elif current_entries:
                # append to last entry's description
                last = current_entries[0]
                if len(current_line) > 10:
                    combined = (last.get("description", "") + " " + current_line).strip()
                    last["description"] = combined[:350]
            else:
                # standalone bullet or sentence
                clean = current_line.replace("•", "").strip()
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
        seen.add(key)
        cleaned.append({
            "description": desc,
            "company": e.get("company"),
            "duration": e.get("duration")
        })
    return cleaned[:6]  # limit noise