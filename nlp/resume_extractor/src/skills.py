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
    #create object of PhraseMatcher
    matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
    skills = load_skills()
    
    patterns = [nlp.make_doc(skill) for skill in skills]
    # load lines that has skills 
    matcher.add("SKILLS", patterns)
    
    matches = matcher(doc)
    extracted = [] # replace it with set 
    # //extract exact skill 
    for _, start, end in matches:
        skill = doc[start:end].text
        if skill not in extracted:
            extracted.append(skill)
    
    return extracted