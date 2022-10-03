# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

import math
import random

size = int(input(" Input size of list: "))
def RandList(list):
    list = []
    for i in range(size):
        list.append(round(random.uniform(0.01, 10.99),2))
    return list    
    
list = RandList(list)
print(list)

def Find(list):
    mx = 0
    mxIndex = 0
    mnIndex = 0
    dif = 0
    mn,mn2 = math.modf(list[0])
    temp = 0
    for i in list:
        temp,temp2 = math.modf(i)
        if temp > mx:
            mx = round((temp),2)
            mxIndex = i
        elif temp < mn:
            mn = round((temp),2)
            mnIndex = i
    dif = mx - mn
    return mx, mn, round((dif),2), mxIndex, mnIndex

returnValues = Find(list)

print(f" Max is {returnValues[0]} in {returnValues[3]}, min is {returnValues[1]} in {returnValues[4]} and difference between them = {returnValues[2]}")
