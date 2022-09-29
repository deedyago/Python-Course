# Реализуйте алгоритм перемешивания списка -*- coding: cp1251 -*-
from random import shuffle
from random import randrange

list = []
for i in range(10):
    list.append(randrange(100))

print(list)
shuffle(list)
print(list)
