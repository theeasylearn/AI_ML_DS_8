import requests
from bs4 import BeautifulSoup
from gtts import gTTS
from io import BytesIO
import pygame
import time
url = 'https://www.divyabhaskar.co.in/rashifal/13/today/'
response = requests.get(url)
if response.status_code == 200:
    print('data found')
    print("_"*100)
    # print(response.text)
    soup = BeautifulSoup(response.text,'html.parser')
    # print(soup.prettify())
    #fetch all paragraphs from div tag whose class name is a6b3d8fe 
    paragraphs = soup.find_all("div", class_="a6b3d8fe")
    result = ''
    for item in paragraphs:
        result += item.get_text(strip=True)
    # print(result)
    tts = gTTS(text=result, lang='gu', slow=False)
    tts.save("my_gujarati_horoscope.mp3")
    mp3_buffer = BytesIO()
    tts.write_to_fp(mp3_buffer)
    mp3_buffer.seek(0)           # important: go back to start

    # Initialize pygame mixer (only once is enough)
    pygame.mixer.init()
    pygame.mixer.music.load(mp3_buffer, 'mp3')
    pygame.mixer.music.play()

    # Optional: wait until sound finishes (if you want script to wait)
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    print("Playback finished (played in background, no window)")
else:
    print("operation failed ",response.status_code)