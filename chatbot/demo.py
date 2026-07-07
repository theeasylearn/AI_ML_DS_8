# access particular key and its value 
import knowledge_base as k
question = input("What is your question>")
for topic in k.knowledge['topics']:
    for item in k.knowledge['topics'][topic]:
       if item == "keywords":
           for key in k.knowledge['topics'][topic]['keywords']:
               if question == key:
                    print(k.knowledge['topics'][topic]['answer'])
                    exit(0)