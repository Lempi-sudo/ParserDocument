#Вариант 2.
#Создать текстовый документ и наполнить его любым текстом, состоящим хотя бы из 1000 слов.
#Реализовать программу, считывающую текст из этого документа, подсчитывающую количество букв
# в нём и сохраняющую в выходной файл статистику по всему алфавиту.

import re

def ReadText(filename):
    with open(filename ,mode='r' , encoding="utf8") as file:
        text=file.read()
    return text

def parseword(text,pattern):
    allres = re.findall(pattern, text)
    return allres

def lowRegist(text):
    lowtext=[]
    for word in text:
        lowtext.append(word.lower())
    return lowtext

def listChar(listWords):
    listchar=[]
    for word in listWords:
        for char in word:
            listchar.append(char)
    return listchar

def dictCharRepit(listChar):
    repitchar = {}
    for char in listChar:
        if char not in repitchar:
            repitchar[char] = int(1)
        else:
            repitchar[char] += 1
    return repitchar

def WriteFile(listrepitchar , filename ):
    with open(filename,'w', encoding="utf8") as file:
        file.write('Самые часто встречающиеся ,буквы  в файле\n')
        sort_list=sorted(listrepitchar.items(), key=lambda k:k[0] , reverse=False)
        file.write('буква \t количество букв\t\n')
        for para in sort_list:
            file.write(para[0]+'=' +str(para[1])+'\n')

if __name__ == '__main__':
    text=ReadText('text.txt')
    lookfor = r"[а-яА-Я]+"
    listword=parseword(text,lookfor)
    listwordlow=lowRegist(listword)
    listchar=listChar(listwordlow)
    dictchar=dictCharRepit(listchar)
    WriteFile(dictchar,'char.txt')
