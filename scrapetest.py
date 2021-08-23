#https://realpython.com/python-web-scraping-practical-introduction/
# Не самый надежный способ извлечения текста из html

from urllib.request import urlopen

#url = "http://olympus.realpython.org/profiles/aphrodite"
url = "http://olympus.realpython.org/profiles/poseidon"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode('UTF-8')
print(html)

print('-' * 25)
title_index = html.find("<title>")
print(title_index)

start_index = title_index + len('<title>')
print('-' * 25)
print(start_index)

end_index = html.find('</title>')
print('-' * 25)
print(end_index)

title = html[start_index:end_index]
print('-' * 25)
print(title)

# Извлечение данных посредством регулярных выражений
