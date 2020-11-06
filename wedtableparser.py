#Сохранить в текстовый документ код какой-либо html-страницы, содержащей таблицу,
# например, http://frs24.ru/st/tablica-kalorijnosti-produktov-pitaniya/.
#Прочитать при помощи регулярных выражений содержимое этой таблицы,
# собрать информацию в какую-либо структуру данных. И сделать вывод в выходной файл.

import requests
import re
from bs4 import BeautifulSoup
from sys import getdefaultencoding


URL='http://frs24.ru/st/tablica-kalorijnosti-produktov-pitaniya'
HEADERS ={'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36 OPR/72.0.3815.148 (Edition Yx 02)' ,'accept': '  */*' }

URLFOOTBAL='https://football-match24.com/vse-chempiony-mira-po-futbolu-tablica-pobeditelej-po-godam.html'

def get_html(url):
    r=requests.get(url)
    return r

def parse():
    html=get_html(URL)
    text=html.text
    return text



if __name__ == '__main__':
    parse()


