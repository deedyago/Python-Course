# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

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
