#Сохранить в текстовый документ код какой-либо html-страницы, содержащей таблицу,
# например, http://frs24.ru/st/tablica-kalorijnosti-produktov-pitaniya/.
#Прочитать при помощи регулярных выражений содержимое этой таблицы,
# собрать информацию в какую-либо структуру данных. И сделать вывод в выходной файл.

import requests
import re
from bs4 import BeautifulSoup
from sys import getdefaultencoding

#кодировка windows-1251 считывает контент некорректоно
URLFOOD='http://frs24.ru/st/tablica-kalorijnosti-produktov-pitaniya'


#кодировка utf-8 считывает контент корректоно
URLFOOTBAL='https://football-match24.com/vse-chempiony-mira-po-futbolu-tablica-pobeditelej-po-godam.html'

def get_html(url):
    r=requests.get(url)
    return r

def parse():
    html=get_html(URLFOOD)
    e=html.encoding
    print(e) # вывод: ISO-8859-1
    text=html.text


    return



if __name__ == '__main__':
    parse()


