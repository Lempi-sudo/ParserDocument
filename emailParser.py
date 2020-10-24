
def ReadFile(filename):
    with open(filename,"r", encoding="utf8") as myfile:
        string=myfile.readlines()
    return string


def textcreate(liststring):
    t = ''
    for string in liststring:
        t += string
    return t


if __name__ == '__main__':
    text=ReadFile('email.txt')

    textlookfor=r"[п]\w{6}\s"


