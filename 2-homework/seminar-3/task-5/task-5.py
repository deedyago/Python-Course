# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

size = int(input(" Input size of fibonacci line: "))

def FibonacciList(size):
    fibList = [-1,0,1]
    for i in range(3,size*2,2):
        fibList.append(fibList[i-1]+fibList[i-2])
        fibList.insert(0,fibList[i]*-1)
    return fibList

print(FibonacciList(size))


