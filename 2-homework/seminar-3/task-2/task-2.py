# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import randrange
size = int(input(" Input size of list: "))

def RandList(list,size):
    list = []
    for i in range(size):
        list.append(randrange(10))
    return list
    
list = RandList(list,size)

def Smth(list):
    list2= []
    tempOp = 0
    for i in range(size//2 + 1):
        tempOp = list[i] * list[size-i-1]
        list2.append(tempOp)
    return list2

list2 = Smth(list)

print(list, "\n",list2)
