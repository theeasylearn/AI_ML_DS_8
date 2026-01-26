'''
write a program to accept birth day and birth month from user as separate input. decide zodiac sign from below table 
    1 Aries: March 21–April 19
    2 Taurus: April 20–May 20
    3 Gemini: May 21–June 21
    4 Cancer: June 22–July 22
    5 Leo: July 23–August 22
    6 Virgo: August 23–September 22
    7 Libra: September 23–October 22
    8 Scorpio: October 24–November 21
    9 Sagittarius: November 22–December 21
    10 Capricorn: December 22–January 19
    11 Aquarius: January 20–February 18
    12 Pisces: February 19–March 20
'''
zodiac = [None,"Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
day = int(input("Enter day of birth date")) 
month = int(input("Enter month of birth date"))
sign = 0 
#day = 20 month = april
if (month == 3 and day>=21) or (month == 4 and day<=19):
    sign = 1
elif (month == 4 and day>=20) or (month == 5 and day<=20):
    sign = 2
elif (month == 5 and day>=21) or (month == 6 and day<=21):
    sign = 3
elif (month == 6 and day>=22) or (month == 7 and day<=22):
    sign = 4
elif (month == 7 and day>=23) or (month == 8 and day<=22):
    sign = 5
elif (month == 8 and day>=23) or (month == 9 and day<=22):
    sign = 6
elif (month == 9 and day>=23) or (month == 10 and day<=22):
    sign = 7
elif (month == 10 and day>=24) or (month ==11 and day<=21):
    sign = 8
elif (month == 11 and day>=22) or (month == 12 and day<=21):
    sign = 9
elif (month == 12 and day>=22) or (month == 1 and day<=19):
    sign = 10
elif (month == 1 and day>=20) or (month == 2 and day<=18):
    sign = 11
elif (month == 2 and day>=19) or (month == 3 and day<=20):
    sign = 12

print(zodiac[sign])