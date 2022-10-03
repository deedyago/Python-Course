# Ќапишите программу, котора€ будет преобразовывать дес€тичное число в двоичное.

inputNumber = int(input(" Input yr number in decimal numeral system: "))
osnovanie = int(input(" Input numeral system to convert in: "))

def TenDimensionalTo(input, osn):
    sum = 0
    output = ""
    while input > 0:
        sum = input % osn
        input = input // osn
        output = str(sum) + output
    return output

print(f"Equivalent in -{osnovanie}- numeral system of your number -{inputNumber}- in decimal numeral system is => {TenDimensionalTo(inputNumber,osnovanie)}")