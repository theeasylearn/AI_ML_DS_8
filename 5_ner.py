import nltk

from nltk.tokenize import word_tokenize
text = """John Smith, a software engineer from Ahmedabad, works at Google and recently visited Mumbai on 15 August 2025. He booked a room at the Taj Mahal Palace Hotel and paid ₹12,500 using his Visa card ending in 4587. His email address is [john.smith@gmail.com](mailto:john.smith@gmail.com), and his phone number is +91-9876543210. During the trip, he attended the India Tech Summit and met representatives from Microsoft, Amazon, and Infosys. He later traveled to New Delhi by Air India flight AI302 and stayed near India Gate. His office address is 101 Business Park, SG Highway, Ahmedabad, Gujarat, 380015. The project budget was $50,000, and the contract reference number was CT-2025-78945. His website is [www.johnsmith.dev](http://www.johnsmith.dev), and his employee ID is EMP10234."""

tokens = word_tokenize(text)
print(tokens)

pos_tags = nltk.pos_tag(tokens)
print(pos_tags)

entities = nltk.ne_chunk(pos_tags)
print(entities)
