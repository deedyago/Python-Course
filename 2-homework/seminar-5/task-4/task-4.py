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
    outputFile = open("EncodedFile.txt","w")
    outputFile.write(output)
    outputFile.close()
    return output

def FileOpen(file):
    inputFile = open(f"{file}","r")
    output = inputFile.readline()
    return output
    inputFile.close()

def Decode(inputData):
    output = ''
    count = ''
    for char in inputData:
        if char.isdigit():
            count += char
        else:
            output += char * int(count)
            count = ''
    outputFile = open("DecodedFile.txt","w")
    outputFile.write(output)
    outputFile.close()
    return output

print(Encode(FileOpen("toEncodeFile.txt")))
print(Decode(FileOpen("EncodedFile.txt")))
