#Создать текстовый документ и наполнить его любым текстом, состоящим хотя бы из 1000 слов.
#Реализовать программу, считывающую текст из этого документа,
# подсчитывающую количество слов в нём
# и сохраняющую в выходной файл N (задаётся пользователем) наиболее часто встречаемых слов.

def readFile(Filename):
    with open(Filename,"r", encoding="utf8") as myfile:
        strings = myfile.readlines()
    return strings

def splitStrings(strings):
    split_string = []
    for st in strings:
        split_string.append(st.split())
    return split_string

def wordsFromDocument(filename):
    str=readFile(filename)
    spl_str=splitStrings(str)
    return spl_str

if __name__ == '__main__':
    print(wordsFromDocument("text.txt"))