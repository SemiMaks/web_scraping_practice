#https://realpython.com/python-web-scraping-practical-introduction/
# import re
# from urllib.request import urlopen
#
# url = 'http://olympus.realpython.org/profiles/dionysus'
# page = urlopen(url)
# html = page.read().decode('utf-8')
#
# pattern = '<title.*?>.*?</title.*?>'
# match_results = re.search(pattern, html, re.IGNORECASE)
# title = match_results.group()
# title = re.sub('<.*?>', '', title) # удаление HTML тегов
#
# print(title)

import re
from urllib.request import urlopen

url = 'http://olympus.realpython.org/profiles/dionysus'
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode('UTF-8')

title_index = html.find('<h2>')
start_index = title_index + len('<h2>')
end_index = html.find('</h2>')

title = html[start_index:end_index]
print(title)
