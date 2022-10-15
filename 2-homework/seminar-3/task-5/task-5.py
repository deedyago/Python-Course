# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

size = int(input(" Input size of fibonacci line: "))

def FibonacciList(size):
    fibList = [1,0,1]
    for i in range(3,size*2,2):
        fibList.append(fibList[i-1]+fibList[i-2])
        if i-2 % 2 != 0:
            fibList.insert(0,fibList[i]*-1)
        else:
            fibList.insert(0,fibList[i])
    return fibList

print(FibonacciList(size))

#fib1 = 0
#fib2 = 1
 
#n = int(input())
 
## print(fib1, fib2, end=' ')
#result = str(fib1) + ' ' + str(fib2)
#for i in range(1, n+1):
#    fib1, fib2 = fib2, fib1 + fib2
#    # print(fib2, end=' ')
#    if i == n and i%2!=0:
#        result=str(fib1) + ' ' + result
#    elif i%2==0 and i!=n:
#        result=str(-fib1) + ' ' + result + ' ' + str(fib2)
#    elif i==n and i%2==0:
#        result=str(-fib1) + ' ' + result
#    else:    
#        result=str(fib1) + ' ' + result + ' ' + str(fib2)
#print(result)

