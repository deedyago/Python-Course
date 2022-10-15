# Вычислить число c заданной точностью d - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math


input = int(input(" Input k: "))
while input < 1 or input > 10:
    input = int(input(" Input k: "))
else:
    print(10**-input, "=>", round(math.pi, input))