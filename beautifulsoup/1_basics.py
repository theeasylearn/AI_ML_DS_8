html_doc = """
<html><head><title>this is text inside title</title></head>
<body>
<p class="title"><b>The story of Joy</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Geeta</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Sita</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Laxmi</a>;
and they lived at the bottom of a well.</p>
<p class="story">Read More</p>
"""
# from package import module
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc,'html.parser')
# print(soup.prettify())
print(soup.title) #will print tag & text inside title tag 
print(soup.title.text) #will print text inside title tag 
print(soup.find('p',class_='title').text)
print(soup.find('p',class_='story').text)
#get each and every a tag which has class sister
a_tags = soup.find_all("a", class_="sister")

for a in a_tags:
    print(a.get_text(strip=True))