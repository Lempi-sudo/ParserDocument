#Создать текстовый документ содержащий список адресов электронных почт,
# их можно придумать самому. Количество не менее 50.
#Записать в выходной файл список доменов электронных почт из входного файла.


import re

def ReadFile2(filename):
    with open(filename,"r", encoding="utf8") as myfile:
        text = myfile.read()
    return text

def WriteFile(listemail , filename ):
    with open(filename,'w', encoding="utf8") as file:
        file.write('домены электронной почты : \n')
        n=0
        for email in listemail:
            file.write(email+' ; ')
            n+=1
            if n%5==0:
                file.write('\n')


def ParseEmail(text):
    textlookfor = r"[@][\w-]+\.+[\w.]+"
    allresulr = re.findall(textlookfor, text)
    return allresulr


if __name__ == '__main__':
    text=ReadFile2('email.txt')
    listemail=ParseEmail(text)
    WriteFile(listemail,'emailparse.txt')



