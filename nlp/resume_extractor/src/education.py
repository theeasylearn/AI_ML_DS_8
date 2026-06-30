import re

def extract_education(doc):
    education = []
    degree_keywords = [
    "Percentage", "Aggregate", "First Class with Distinction", "First Class", "Second Class", 
    "Percentile", "Rank", "University Rank Holder", "Branch Rank", "Merit List", "Score", 
    "Valid Score", "Gold Medalist", "Silver Medalist", "Dean's List", "Director's Merit List", 
    "Scholarship Recipient", "KVPY Scholar", "NTSE Scholar", "Institute", "Academy", 
    "Affiliated to", "Approved by", "Recognized by", "AICTE", "UGC", "NAAC Accredited", 
    "Autonomous Institute", "MHRD", "Ministry of Education", "MoE", "NIRF Ranked", "HSC", 
    "SSC", "AISSCE", "AISSE", "Stream", "Science Stream", "Commerce Stream", "Arts Stream", 
    "Humanities Stream", "CBSE", "ICSE", "IB", "State Board", "PCM", "PCMB", "Final Year Project", 
    "Major Project", "Mini Project", "Seminar", "Electives", "Core Electives", "Professional Electives", 
    "Specialization", "Branch", "Industrial Visit", "Vocational Training", "Dissertation", "Thesis", 
    "Paper Publication", "IEEE", "Springer", "Academic Profile", "Educational Qualifications"]

    for sent in doc.sents:
        text = sent.text.strip().lower()
        # text = text.lower()
        if any(keywords.lower() in text for keywords in degree_keywords):
            year = re.search(r'(19|20)\d{2}',text)
            education.append({
                "degree": text[:280],
                "year": year.group() if year else None
            })
    
    return education