import spacy
from spacy.matcher import PhraseMatcher

nlp = spacy.load("en_core_web_sm")

def load_skills():
    try:
        #try to load skills from file 
        with open("skills_list.txt", "r", encoding="utf-8") as f:
            #append each and every skill into lines
            lines = []
            for line in f:
                temp = line.strip()
                if temp!=None:
                    lines.append(temp)
            return lines
    except:
        return ["Python", "SQL", "JavaScript", "Machine Learning", "Data Analysis", 
                "Excel", "Power BI", "Git", "Django", "HTML", "CSS", "Leadership"]

def extract_skills(doc):
    # PhraseMatcher from list
    matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
    skills = load_skills()
    
    patterns = [nlp.make_doc(skill) for skill in skills]
    matcher.add("SKILLS", patterns)
    
    matches = matcher(doc)
    extracted = []
    for _, start, end in matches:
        skill = doc[start:end].text
        if skill not in extracted:
            extracted.append(skill)
    
    # Additional fallback extraction for common technical terms in this resume style
    full = doc.text.lower()
    extra = []
    candidates = ['c ', 'c,', ' c ', 'hdf5', 'computer vision', 'image processing', 'postgre', 'postgresql', 'vs code', 'web security', 'network security', 'bilingual']
    for keyword in candidates:
        if keyword in full:
            nice = keyword.strip().title().replace('Hdf5', 'HDF5').replace('Postgre', 'PostgreSQL').replace('C ', 'C')
            if nice not in extracted and nice not in extra:
                extra.append(nice.strip())
    
    extracted.extend(extra)
    return extracted