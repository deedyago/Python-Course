# ������� ������ �� N ���������, ����������� ������� �� ���������� [-N, N]. 
# ������� ������������ ��������� �� ��������� ��������. ������� �������� � ����� file.txt � ����� ������ ���� �����.

input = int(input(" Input N: "))

array = []

for i in range(input*-1,input+1):
    array.append(i)

with open ('file.txt') as data:
    op = 1
    for line in data.readlines():
        pos = line
        op = array[int(pos)] * op
    print(array, " = ", op)