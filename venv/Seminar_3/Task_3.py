#  В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
#  Не учитывать знаки препинания и регистр символов.
#  За основу возьмите любую статью из википедии или из документации к языку.


import requests
from bs4 import BeautifulSoup
import re


def parsing_page(url):
    '''
    Функция позволяет получить информацию со страницы и вернуть текст.
    :param url:
    '''
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.find('div', class_='mw-parser-output').text
    return text


text = parsing_page('https://ru.wikipedia.org/wiki/Python')
print(text)

# разбиение текста по словам
words = re.findall(r'\w+', text)
words_dict = {}

# подсчет количества встречаемости слов
for word in words:
    if word in words_dict:
        words_dict[word] += 1
    else:
        words_dict[word] = 1

# сортировка и вывод
words_dict = sorted(words_dict.items(), key=lambda x: x[1], reverse=True)
print(words_dict[:10])
