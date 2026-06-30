experience_header = [
    "Professional Experience", "Work Experience", "Employment History", "Work History", 
    "Professional Background", "Career History", "Career Progression", "Experience", 
    "Relevant Experience", "Technical Experience", "Professional Profile", "Industry Experience", 
    "Employment Details", "Job History", "Corporate Experience", "Hands-on Experience"
]
def extract_experience(doc):
    experience = []
    exp_section = False
    for sent in doc.sents:
        text = sent.text.strip()
        text = text.lower()
        
        # Detect start of experience section
        if any(word.lower() in text for word in experience_header):
            exp_section = True
            if len(text) > 25:
                experience.append({
                    "description": text[:300],
                    "company": None,
                    "duration": None
                })   
                        #  task detect company name and duration 
    return experience