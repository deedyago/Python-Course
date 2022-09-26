# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input("Input number of quarter: "))

def RangeOfQ(q):
    if q == 1:
        return "from x = 1 to infinity and y = 1 to infinity"
    if q == 2:
        return "from x = -1 to -infinity and y = 1 to infinity"
    if q == 3:
        return "from x = -1 to -infinity and y = -1 to -infinity"
    if q == 4:
        return "from x = 1 to infinity and y = -1 to -infinity"


if quarter < 1 or quarter >4:
    print("Input is mistaken")
else:
    print(f" Range of numbers in {quarter} quarter can be {RangeOfQ(quarter)}")