# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции
from random import randrange

list = []
size = int(input(" Input size of list: "))

def RandList(list,size):
    for i in range(size):
        list.append(randrange(10))
    return list
    
list = RandList(list,size)

def Smth(list):
    sum = 0
    for i in range(0,size,2):
        sum = sum + list[i]
    return sum

print(list, Smth(list))