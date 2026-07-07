import spacy as sa 
#load model
nlp = sa.load('en_core_web_sm')
#create doc object 
paragraph ="""
i am student. i am from Bhavnagar to Ahmedabad to attend a technology conference organized by The Easylearn Academy. During the event, he met Priya Shah, a software engineer from Infosys, and Michael Johnson, a researcher from Stanford University. They discussed artificial intelligence projects funded by Google and Microsoft with a budget of ₹50 lakh. The conference was held on 15 June 2026 at the Mahatma Mandir Convention Centre in Gandhinagar, Gujarat, India. Later, the team booked rooms at the Taj Hotel and planned a visit to New Delhi before flying to the United States on 20 June 2026."""
doc = nlp(paragraph)

lexem = doc[1]
print("Lexem:", lexem)
print("text:", lexem.text)
print("lower_:", lexem.lower_)
# print("upper_:", lexem.upper_)
print("is_alpha:", lexem.is_alpha)
print("is_stop:", lexem.is_stop)
print("is_digit:", lexem.is_digit)