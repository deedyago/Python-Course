# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

def MchelSum(f):
    file = open(f,"r")
    list1 = str(file.readline()).split('x')
    c=b=a = 0
    if len(list1) == 3:
        c = list1[2][1:]
    if len(list1) >= 2:
        b = list1[1][3:-1]
    a = list1[0][:-1]
    return a,b,c
    file.close()


def Sborka(a, b, c, out=''):
    if b > 0:
        out += "+" + str(b) + "*x"
    if c > 0:
        out += "+" + str(c)
    return f"{a}*x^2" + out


file1 = "MChel1.txt"
file2 = "MChel2.txt"

a1,b1,c1 = MchelSum(file1)
a2,b2,c2 = MchelSum(file2)

fileOutput = open("MchelSum","w")
fileOutput.write(Sborka(int(a1) + int(a2), int(b1) + int(b2), int(c1) + int(c2)))
#print(Sborka(int(a1) + int(a2), int(b1) + int(b2), int(c1) + int(c2)))
fileOutput.close()


