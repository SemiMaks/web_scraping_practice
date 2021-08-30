from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'http://olympus.realpython.org/profiles/dionysus'
page = urlopen(url)
html = page.read().decode('UTF-8')
soup = BeautifulSoup(html, 'html.parser')

print(soup.get_text().replace(' ', '')) # метод .get_text удаляет все теги из soup

print(soup.find_all('img')) # возвращает список всех <img> тегов в документе HTML
image1, image2 = soup.find_all('img')
print(image1.name, image2.name)
print(image1['src'], image2['src'])
print(soup.title)


