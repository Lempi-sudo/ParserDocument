#4 Создать текстовый документ содержащий список телефонных номеров, часть из которых будет невалидна.
#  Записать в выходной файл только валидные телефонные номера (номер должен быть длиной 10 знаков и начинаться с 9
#  или длиной 11 знаков и начинаться с 8 или 7).

import re
from emailParser import *


def ParseNumberPhone(text):
    textlookfor =r"[87][0-9]{10}[\s,.\n]|" \
                 r"[9][0-9]{9}[\s,.\n]|" \
                 r"[87][(][0-9]{3}[)][0-9]{7}[\s.,\n]|" \
                 r"[(][9][0-9]{2}[)][0-9]{3}[-][0-9]{2}[-][0-9]{2}[\s.,\n]|" \
                 r"[78][(][0-9]{3}[)][0-9]{3}[-][0-9]{2}[-][0-9]{2}[\s\n.,]"
    allresulr = re.findall(textlookfor, text)
    return allresulr

def WriteFile(listemail , filename ):
    with open(filename,'w', encoding="utf8") as file:
        file.write('номера телефонов : \n')
        n=0
        for email in listemail:
            file.write(email+' ; ')
            n+=1
            if n%5==0:
                file.write('\n')



if __name__ == '__main__':
    text = ReadFile('numberphonedoc.txt')
    listphone = ParseNumberPhone(text)
    WriteFile(listphone, 'parsephonenumber.txt')




