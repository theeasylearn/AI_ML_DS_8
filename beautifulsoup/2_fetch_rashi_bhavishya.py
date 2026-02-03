import requests
from bs4 import BeautifulSoup
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
    
    print(result)
else:
    print("operation failed ",response.status_code)