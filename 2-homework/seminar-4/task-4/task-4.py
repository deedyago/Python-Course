# ������ ����������� ������� k. ������������ ��������� ������� ������ ������������� (�������� �� 0 �� 100) ���������� � �������� � ���� ��������� ������� k.
from random import randint

k = int(input(" Input K: "))
file = open("file.txt", "w")
def MChel(k):
    output = list()
    tempK = k
    while tempK!=-1:
        if tempK > 1:
            file.write(str(randint(2,10)))
            file.write("x^")
            file.write(str(tempK))
            file.write(" + ")
            tempK -=1
        elif tempK == 1:
            file.write(str(randint(2,10)))
            file.write("x")
            file.write(" + ")
            tempK -=1
        elif tempK == 0:
            file.write(str(randint(2,10)))
            file.write(" = 0")
            tempK -=1
    file.close()

MChel(k)

