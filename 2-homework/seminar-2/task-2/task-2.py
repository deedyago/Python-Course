# �������� ���������, ������� ��������� �� ���� ����� N � ������ ����� ������������ ����� �� 1 �� N.

input = int(input(" Input N: "))

def OpRange(input):
    op = 1
    array = [0] * input
    for i in range(input):
        op = (i+1)*op
        array[i] = op
    return array

outArray = OpRange(input)
print(outArray)
