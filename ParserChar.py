#Вариант 2.
#Создать текстовый документ и наполнить его любым текстом, состоящим хотя бы из 1000 слов.
#Реализовать программу, считывающую текст из этого документа, подсчитывающую количество букв
# в нём и сохраняющую в выходной файл статистику по всему алфавиту.

from parserword import *

def listChar(listWords):
    listchar=[]
    for word in listWords:
        for char in word:
            listchar.append(char)
    return listchar

def lowRegist(text):
    lowtext=[]
    for word in text:
        lowtext.append(word.lower())
    return lowtext

def onlyLetter(listCharacter):
    listletter=[]
    for char in listCharacter:
        if char.isalpha():
            listletter.append(char)
    return listletter


def WriteFile(listrepitchar , filename ):
    with open(filename,'w', encoding="utf8") as file:
        file.write('Самые часто встречающиеся ,буквы  в файле\n')
        sort_list=sorted(listrepitchar.items(), key=lambda k:k[0] , reverse=False)
        file.write('буква \t количество букв\t\n')
        for para in sort_list:
            file.write(para[0]+'=' +str(para[1])+'\n')


if __name__ == '__main__':
    listwords = listWordsFromDocument('text.txt')
    listwords=lowRegist(listwords)

    listchar = listChar(listwords)
    listletter=onlyLetter(listchar)

    dictletter=dictwordRepetitionСounting(listletter)

    WriteFile(dictletter,'parseletter.txt')



