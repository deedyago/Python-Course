# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


n = int(input(" Input N: "))
number = 2
list = list()

def IfSimple(inp):
    sc = 0
    for i in range(2, inp // 2+1):
        if (a % i == 0):
            sc += 1
        if (k <= 0):
            return True
        else:
            return False


def List(input):
    while n != 1:
        if n % number == 0 and IfSimple(number) == True:
            n /= number
            list.append(number)
        else:
            number += 1
    return list


print(List(list))