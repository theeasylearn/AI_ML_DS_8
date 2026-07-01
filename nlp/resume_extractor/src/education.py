import re

def extract_education(doc):
   
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
    "Specialization", "Branch", "Industrial Visit", "Vocational Training", "Dissertation", "Thesis", 'MCA', 'BCA', 'BBA', 'MBA', 'BE-IT', 'BE-EC', 'BE-CE', 'ME-IT', 'ME-CE', 'M.Tech', 'B.tech',"Paper Publication", "IEEE", "Springer", "Academic Profile", "Educational Qualifications"]
    education = [] #empty list
    for sentence in doc.sents:
        text = sentence.text.strip().lower()
        # text = text.lower()
        for keywords in degree_keywords:
            if keywords.lower() in text:
                year = re.search(r'(19|20)\d{2}',text)    
                education.append({
                "degree": text[:280],
                "year": year.group() if year else None
            })
    return education