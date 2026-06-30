# src/extractor.py

import sys
import os
# Add parent directory to path so it can find modules inside src
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.preprocess import preprocess_resume
from src.contact import extract_contact_info
from src.skills import extract_skills
from src.education import extract_education
from src.experience import extract_experience
from src.certification import extract_certifications


#this is the controller (brain of the application)
def extract_resume(text, filename=""):
    """Main resume extraction pipeline"""
    doc = preprocess_resume(text) #return doc object after removing extra space and newline

    #create dictionary that has keys 
    '''
        filename 
        contact
        skills
        education
        experience 
        certification

    '''
    result = {
        "filename": filename,
        "contact": extract_contact_info(doc),
        "skills": extract_skills(doc),
        "education": extract_education(doc),
        "experience": extract_experience(doc),
        "certifications": extract_certifications(doc),
        "extracted_at": "2026"
    }
    
    return result