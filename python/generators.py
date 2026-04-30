import random as rd 
import string as st 
def getOTP(length=6):
    digit = '' #string
    for i in range(0,length):
        digit += str(rd.randint(0,9))
    return digit

def getRandomPassword(length=6):
    seeds = st.ascii_lowercase + st.ascii_uppercase + st.digits + st.punctuation
    #convert seeds into list 
    seeds = list(seeds)
    #list shuffle 
    rd.shuffle(seeds)
    size = len(seeds)
    password = [] #empty list 
    for i in range(0,length):
        password.append(seeds[rd.randint(0,size-1)])
    return ''.join(password)

print(getRandomPassword(10))
print(getRandomPassword(20))
# print(getOTP())
# print(getOTP(4))
# print(getOTP(10))