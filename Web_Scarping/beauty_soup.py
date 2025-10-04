from bs4 import BeautifulSoup
from urllib.request import urlopen
url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
print(soup.get_text())
#print(soup.find_all("img"))
img1, img2 = soup.find_all("img")
print(img1.name)
src = img1["src"]
print(src)
print(soup.title)
print(soup.title.string)
print(soup.find_all("img", src="/static/dionysus.jpg"))