import re #re means regular expression

def extract_contact_info(doc):
    #crete empty dictionary
    info = {"name": None, "email": None, "phone": None, "location": None}
    full_text = doc.text
    # list comprehension
    lines = [line.strip() for line in full_text.split('\n') if line.strip()]

    # Email
    email_match = re.search(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', full_text)
    if email_match != None:
        info["email"] = email_match.group()

    # Phone - support +91 98765 43210, 9876543210, +91-98765-43210, etc.
    phone_patterns = [
        r'\+91[\s-]?(\d{5}[\s-]?\d{5})',           # +91 98765 43210 or +919876543210
        r'\b(\d{5}[\s-]?\d{5})\b',                  # 98765 43210
        r'(\+91|0)?[\s-]?(\d{10})\b'                # 9876543210
    ]
    for pattern in phone_patterns: #search for each and every pattern
        mobile = re.search(pattern, full_text)
        if mobile !=None:
            # Take the captured group that looks like the number
            num = mobile.group(1) or mobile.group(2) or mobile.group(0)
            num = re.sub(r'[\s-]','', num)  # clean
            if len(num) >= 10:
                info["phone"] = num[-10:]   # last 10 digits
                break

    # Location - look in first few lines for "City, State, Country" pattern
    location_patterns = [
        r'([A-Za-z\s]+,\s*[A-Za-z\s]+,\s*India)',
        r'([A-Za-z]+,\s*Gujarat)',
        r'Bhavnagar[^,\n]*',
    ]
    for pat in location_patterns:
        lm = re.search(pat, full_text, re.IGNORECASE)
        if lm:
            loc = lm.group(1) if lm.lastindex else lm.group(0)
            info["location"] = loc.strip()
            break

    # Name - first non-empty line, cleaned
    if lines!=None:
        name_line = lines[0] #assume first line has only name
        #but we have to check 1st line must not have mobile,email links. if it is we have to remove it 
        name_line = re.sub(r'(\+91|0)?[\s-]?\d{5,10}', '', name_line)
        name_line = re.sub(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', '', name_line)
        name_line = re.sub(r'linkedin\.com|github\.com|•', '', name_line, flags=re.IGNORECASE)
        cleaned = name_line.strip()
        if cleaned!=None and len(cleaned) >= 2:
            info["name"] = cleaned
    return info