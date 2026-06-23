import spacy 
from spacy.language import Language
from spacy.tokens import Doc 
nlp = spacy.load('en_core_web_sm')
Doc.set_extension("courses",default=[])

courses = [
    "python",
    "data science",
    "c",
    "c++",
    "java",
    "cyber security",
    "digital marketing"
]
@Language.component("fetchCourse")
def fetchCourse(doc):
    global courses
    #empty list 
    founded_courses = []
    text = doc.text.lower()
    for item in courses:
        if item in text:
            founded_courses.append(item)
    doc._.courses = founded_courses
    return doc 

text = "I want to learn python and data science and c"
nlp.add_pipe("fetchCourse",last=True) # add fetchCourse into pipline 
doc = nlp(text) #it will automatically call fetchCourses function in pipeline 
print(doc._.courses)