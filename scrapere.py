#https://realpython.com/python-web-scraping-practical-introduction/
# Извлечение данных посредством регулярных выражений

import re

print(re.findall("ab*c", "ac")) # начинается с а, имеет ноль или более b заканчивается на с
print(re.findall("ab*c", "abCac", re.IGNORECASE)) # любой регистр
print(re.findall('ab*c', 'abdc')) # нет совпадений
print(re.findall('a.c', 'abc')) # точка вместо любого символа
print(re.findall('a.c', 'abbc')) # нет совпадений, разное количество символов
print(re.findall('a.*c', 'abbc')) # звездочка - любой символ любое количество раз

print(re.search('a.*c', 'abbc')) # возвращает первый результат
match_results = re.search('ab*c', 'ABC', re.IGNORECASE)
print(match_results.group()) # 'ABC'

string = "Everything is <replaced> if it's in <tags>."
string1 = re.sub('<.*>', 'ELEPHANTS', string)
print(string1) # 'Everything is ELEPHANTS.'
# .* - поиск первого совпадения, .? - поиск всех совпадений

string2 = re.sub('<.*?>', 'ELEPHANTS', string)
print(string2) # 'Everything is ELEPHANTS if it's in ELEPHANTS.'

