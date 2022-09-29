# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр -*- coding: cp1251 -*-

input = float(input(" Input your number: "))

def SumOf(input):
    sum = 0
    temp = input
    while input != 0:
        temp = input % 10
        sum = sum + temp
        input = input // 10
    return sum

print(f"Sum of elements in your number {input} is {SumOf(input)}")

########################################### v2

input = input(" Input your number: ")

def SumOf(input):
    input2 = input.replace('.','')
    sum = 0 
    for digit in input2:
        sum = sum + int(digit)
    return sum

print(f"Sum of elements in your number {input} is {SumOf(input)}")