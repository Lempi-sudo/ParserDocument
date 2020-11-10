#Создать текстовый документ и наполнить его любым текстом, состоящим хотя бы из 1000 слов.
#Реализовать программу, считывающую текст из этого документа,
# подсчитывающую количество слов в нём
# и сохраняющую в выходной файл N (задаётся пользователем) наиболее часто встречаемых слов.
import re

def ReadText(filename):
    with open(filename ,mode='r' , encoding="utf8") as file:
        text=file.read()
    return text

def parseword(text):
    lookfor = r"[а-яА-Я]+"
    allres = re.findall(lookfor, text)
    return allres

def dictwordrepit(worldlist):
    repitworld = {}
    for world in worldlist:
        if world not in repitworld:
            repitworld[world] = int(1)
        else:
            repitworld[world] += 1
    return repitworld


def WriteFile(amountworld, listrepitworld, filename ):
    with open(filename,'w', encoding="utf8") as file:
        file.write('количество слов в файле='+str(amountworld)+'\n')
        file.write('Самые часто встречающиеся слова в файле(ТОП 30) \n')
        sort_list = sorted(listrepitworld.items(), key=lambda k: k[1], reverse=True)
        file.write('слово\t количество слов\t\n')
        n = 1
        for para in sort_list:
            if n % 31 == 0:
                break
            file.write(para[0]+'=' + str(para[1])+'\n')
            n += 1


if __name__ == '__main__':
    filenameinput=input("enter file path to read  for example(text.txt):")
    text=ReadText(filenameinput)
    allres=parseword(text)
    dict=dictwordrepit(allres)
    print(dict)
    filenameoutput = input("enter file path to write:")
    WriteFile(len(allres),dict, filenameoutput )




