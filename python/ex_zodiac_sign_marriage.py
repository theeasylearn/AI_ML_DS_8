'''
write a program for male female marriage compatibility as per below link,  accept birth day and birth month from user as separate input. decide zodiac male_sign as per previous example and then use zodiac male_sign to decide  marriage compatibility

https://miro.medium.com/v2/resize:fit:1100/format:webp/1*f58HMTVzfN2XvCPR23wXgA.jpeg 
'''
zodiac = [None,"Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
print("Enter details for male ")
day = int(input("Enter day of birth date")) 
month = int(input("Enter month of birth date"))
male_sign = 0 
#day = 20 month = april
if (month == 3 and day>=21) or (month == 4 and day<=19):
    male_sign = 1
elif (month == 4 and day>=20) or (month == 5 and day<=20):
    male_sign = 2
elif (month == 5 and day>=21) or (month == 6 and day<=21):
    male_sign = 3
elif (month == 6 and day>=22) or (month == 7 and day<=22):
    male_sign = 4
elif (month == 7 and day>=23) or (month == 8 and day<=22):
    male_sign = 5
elif (month == 8 and day>=23) or (month == 9 and day<=22):
    male_sign = 6
elif (month == 9 and day>=23) or (month == 10 and day<=22):
    male_sign = 7
elif (month == 10 and day>=24) or (month ==11 and day<=21):
    male_sign = 8
elif (month == 11 and day>=22) or (month == 12 and day<=21):
    male_sign = 9
elif (month == 12 and day>=22) or (month == 1 and day<=19):
    male_sign = 10
elif (month == 1 and day>=20) or (month == 2 and day<=18):
    male_sign = 11
elif (month == 2 and day>=19) or (month == 3 and day<=20):
    male_sign = 12

print(zodiac[male_sign])

#female
print("Enter details for male ")
day = int(input("Enter day of birth date")) 
month = int(input("Enter month of birth date"))
female_sign = 0 
#day = 20 month = april
if (month == 3 and day>=21) or (month == 4 and day<=19):
    female_sign = 1
elif (month == 4 and day>=20) or (month == 5 and day<=20):
    female_sign = 2
elif (month == 5 and day>=21) or (month == 6 and day<=21):
    female_sign = 3
elif (month == 6 and day>=22) or (month == 7 and day<=22):
    female_sign = 4
elif (month == 7 and day>=23) or (month == 8 and day<=22):
    female_sign = 5
elif (month == 8 and day>=23) or (month == 9 and day<=22):
    female_sign = 6
elif (month == 9 and day>=23) or (month == 10 and day<=22):
    female_sign = 7
elif (month == 10 and day>=24) or (month ==11 and day<=21):
    female_sign = 8
elif (month == 11 and day>=22) or (month == 12 and day<=21):
    female_sign = 9
elif (month == 12 and day>=22) or (month == 1 and day<=19):
    female_sign = 10
elif (month == 1 and day>=20) or (month == 2 and day<=18):
    female_sign = 11
elif (month == 2 and day>=19) or (month == 3 and day<=20):
    female_sign = 12

print(zodiac[female_sign])
compatibility = [
    None,
    # Female Aries
    [2, 2, 2, 0, 1, 0, 2, 2, 2, 0, 0, 1],
    # Female Leo
    [2, 2, 2, 1, 0, 0, 2, 2, 2, 1, 1, 1],
    # Female Sagittarius
    [2, 2, 2, 0, 0, 0, 2, 2, 2, 1, 1, 1],
    # Female Taurus
    [0, 1, 0, 2, 2, 2, 0, 0, 1, 0, 2, 2],
    # Female Virgo
    [0, 1, 0, 2, 2, 2, 0, 0, 1, 2, 2, 1],
    # Female Capricorn
    [0, 1, 0, 2, 2, 2, 0, 1, 0, 2, 2, 2],
    # Female Gemini
    [2, 2, 1, 0, 1, 1, 2, 2, 2, 0, 0, 0],
    # Female Libra
    [1, 2, 2, 1, 0, 0, 2, 2, 2, 0, 0, 1],
    # Female Aquarius
    [2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 1, 1],
    # Female Cancer
    [0, 1, 1, 2, 2, 2, 0, 0, 0, 2, 2, 2],
    # Female Scorpio
    [1, 1, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2],
    # Female Pisces
    [1, 1, 1, 2, 1, 2, 0, 0, 0, 2, 2, 2]
]
score = compatibility[male_sign][female_sign]    
if score == 2:
    print ("Great Match ♥")
elif score == 1:
    print ("Favorable Match 👍")
else:
    print ("Not Favorable ×")
