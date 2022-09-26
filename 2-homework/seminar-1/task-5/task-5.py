# Ќапишите программу, котора€ принимает на вход координаты двух точек и находит рассто€ние между ними в 2D пространстве

def Coords():
    coord = ["x","y"]
    coord[0] = int(input("Input x: "))
    coord[1] = int(input("Input y: "))
    return coord


def Distance(coord1,coord2):
     distance = ((coord2[0] - coord1[0]) ** 2 + (coord2[1] - coord1[1]) ** 2) ** (0.5)
     return distance

print(" Input coordinates of point A")
coord1 = Coords()
print("Input coordinates of point B")
coord2 = Coords()

print(f" Distance between {coord1} and {coord2} is {round(Distance(coord1,coord2),3)}")
