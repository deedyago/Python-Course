# Напишите программу, удаляющую из текста все слова, содержащие ""абв"

print(list(filter(lambda i: "abv" not in i, str(input("Input words: ")).split())))

