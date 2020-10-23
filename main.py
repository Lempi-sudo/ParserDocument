#Создать текстовый документ и наполнить его любым текстом, состоящим хотя бы из 1000 слов.
#Реализовать программу, считывающую текст из этого документа,
# подсчитывающую количество слов в нём
# и сохраняющую в выходной файл N (задаётся пользователем) наиболее часто встречаемых слов.





def listWordsFromDocument(filename):
    string = readFile(filename)
    spl_str = splitStrings(string)
    worlds = listworld(spl_str)
    return worlds


def readFile( filename ):
    with open(filename,"r", encoding="utf8") as myfile:
        strings = myfile.readlines()
    stringWithoutPunctuationSumbol=deletePunctuationSumbol(strings)
    return stringWithoutPunctuationSumbol

def deletePunctuationSumbol(str):
    for i in range(len(str)):
        str[i] = str[i].replace(':','')
        str[i] = str[i].replace(',', '')
        str[i] = str[i].replace('.', '')
        str[i] = str[i].replace('!', '')
        str[i] = str[i].replace('?', '')
        str[i] = str[i].replace('&', '')
        str[i] = str[i].replace('"', '')
        str[i] = str[i].replace(';', '')
        str[i] = str[i].replace('(', '')
        str[i] = str[i].replace(')', '')
        str[i]=str[i].replace('-', ' ')
        str[i] = str[i].replace('—', ' ')
    return str

def splitStrings(strings):
    split_string = []
    for st in strings:
        split_string.append(st.split())
    return split_string

def numbercWordinFile(filename):
    listworld = listWordsFromDocument(filename)
    number = len(listworld)
    return number


def dictwordRepetitionСounting(worldlist):
    repitworld = {}
    for world in worldlist:
        if world not in repitworld:
            repitworld[world] = int(1)
        else:
            repitworld[world] += 1
    return repitworld

#возвращает список слов
def listworld(text):
    listWord = []
    for string in text:
        for world in string:
            listWord.append(world)
    return listWord

def WriteFile( amoutworld , listrepitworld , filename ):
    with open(filename,'w', encoding="utf8") as file:
        file.write('количество слов в файле='+str(amoutworld)+'\n')
        file.write('Самые часто встречающиеся слова в файле\n')
        sort_list=sorted(listrepitworld.items(), key=lambda k:k[1] , reverse=True)
        file.write('слово\t количество слов\t\n')
        for para in sort_list:
            file.write(para[0]+'=' +str(para[1])+'\n')






if __name__ == '__main__':

    filename=input('enter file name:')

    dict=dictwordRepetitionСounting(listWordsFromDocument(filename))

    WriteFile(numbercWordinFile(filename),dict,'res.txt')




