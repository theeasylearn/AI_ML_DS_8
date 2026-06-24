import spacy 
import re 
from spacy.language import Language
from spacy.tokens import Doc 
nlp = spacy.load('en_core_web_sm')
# add new property to nlp.doc object 
Doc.set_extension("emails",default=[])
Doc.set_extension("mobile",default=[])

#create custom component(function) this function must have doc object as input
@Language.component("fetchEmails")
def fetchEmails(doc):
    text = doc.text
    # Comprehensive email regex pattern
    email_pattern = r'''
        [a-zA-Z0-9._%+-]+      # Local part (username)
        @                      # @ symbol
        [a-zA-Z0-9.-]+         # Domain name
        \.                     # Dot
        [a-zA-Z]{2,}           # Top-level domain
    '''
    # Find all matches (case insensitive)
    emails = re.findall(email_pattern, text, re.IGNORECASE | re.VERBOSE)
    doc._.emails = emails
    return doc 

text = """Hello, you can contact us at support@example.com or 
    sales@company.co.in. Also reach out to admin@sub.domain.org
    or invalid-email@com (this should not match).
    My personal email is john.doe123+test@my-domain.com"""
nlp.add_pipe("fetchEmails",last=True) # add fetchCourse into pipline 
doc = nlp(text) #it will automatically call fetchCourses function in pipeline 
print(doc._.emails)