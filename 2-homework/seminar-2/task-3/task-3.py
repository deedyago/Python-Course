# ������� ������ �� n ����� ������������������ (1+1/n)**n � �������� �� ����� �� �����.

input = int(input(" Input N: "))

def Func(input):
    temp = 0
    sum = 0
    array = [0] * input
    for i in range(1,input+1):
        temp = round((1+1/i)**i)
        sum = sum + temp
        array[i-1] = temp
    return array,sum

array,sum = Func(input)
print(array," = ",sum)