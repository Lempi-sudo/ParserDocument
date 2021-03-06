#Создать текстовый документ содержащий список адресов электронных почт,
# их можно придумать самому. Количество не менее 50.
#Записать в выходной файл список доменов электронных почт из входного файла.


import re

def ReadFile(filename):
    with open(filename,"r", encoding="utf8") as myfile:
        text = myfile.read()
    return text

def WriteFile(listemail , filename ):
    with open(filename,'w', encoding="utf8") as file:
        file.write('домены электронной почты : \n')
        for email in listemail:
            file.write(email+'\n')


def ParseEmail(text):
    textlookfor = r"[@][\w-]+\.+[\w.]+"
    allresulr = re.findall(textlookfor, text)
    return allresulr


if __name__ == '__main__':
    text=ReadFile('text.txt')
    listemail=ParseEmail(text)
    WriteFile(listemail,'emailparse.txt')
