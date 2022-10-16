# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных

def Encode(inputData):
    output = ''
    prevChar = ''
    count = 1
    for char in inputData:
        if char != prevChar:
            if prevChar:
                output += str(count) + prevChar
            count = 1
            prevChar = char
        else:
            count += 1
    else:
        output += str(count) + prevChar
    return output

print(Encode("AAAAAAAAAAABBBCCCBCBCBBBBCCCD"))


def Decode(inputData):
    output = ''
    count = ''
    for char in inputData:
        if char.isdigit():
            count += char
        else:
            output += char * int(count)
            count = ''
    return output

print(Decode(Encode("\nAAAAAAAAAAABBBCCCBCBCBBBBCCCD")))
