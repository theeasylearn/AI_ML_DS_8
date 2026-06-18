from nltk.stem import PorterStemmer

#create object 
ps = PorterStemmer()

words =  ["running", "runs", "runner", "runners", "walked", "walking", "walks", "walker", "playing", "played", "plays", "player", "studying", "studied", "studies", "studying", "writing", "written", "writes", "writer", "reading", "reads", "reader", "readable", "jumping", "jumped", "jumps", "jumper", "singing", "sang", "sings", "singer", "driving", "driven", "drives", "driver", "talking", "talked", "talks", "talkative", "computing", "computed", "computer", "computation", "connecting", "connected", "connection", "connections", "organizing", "organization"]

# print(ps.stem(words[0])) # running -> run
# print(ps.stem(words[1])) # runs -> run

for item in words:
    print(ps.stem(item))