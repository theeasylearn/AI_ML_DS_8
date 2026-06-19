import spacy as sa 
#load model
nlp = sa.load('en_core_web_sm')
#create doc object 
paragraph ="""
i am student. i am from Bhavnagar to Ahmedabad to attend a technology conference organized by The Easylearn Academy. During the event, he met Priya Shah, a software engineer from Infosys, and Michael Johnson, a researcher from Stanford University. They discussed artificial intelligence projects funded by Google and Microsoft with a budget of ₹50 lakh. The conference was held on 15 June 2026 at the Mahatma Mandir Convention Centre in Gandhinagar, Gujarat, India. Later, the team booked rooms at the Taj Hotel and planned a visit to New Delhi before flying to the United States on 20 June 2026."""
doc = nlp(paragraph)
print(f"{'token':<12} {'tag':<12} {'pos':<12} {'leema':<12} {'dependency':<12} {'entity type':<12} is stop word?")
print("_",120)
for token in doc:
    print(f"{token.text:<12} {token.tag_:<12} {token.pos_:<12} {token.lemma_:<12} {token.dep_:<12} {token.ent_type_:<12} {token.is_stop}")
