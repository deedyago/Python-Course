# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
from random import randrange

size = int(input(" Input size of yur list: "))

def randomList(size):
    array = list()
    for i in range(size):
        tempNumber = randrange(1000)
        if tempNumber not in array:
            array.append(tempNumber)
    return array

list = randomList(size)
print(list)