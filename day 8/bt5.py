# Giải và biện luận phương trình bậc nhất một hai ax^2 + bx + c = 0 (ẩn x, a, b, c là ba số cho trước)
import math
print("Equation: ax^2 + bx + c = 0")
a = float(input("Enter a number:"))
b = float(input("Enter b number:"))
c = float(input("Enter c number:"))

if a == 0:
    print("The equation not quadratic")
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        print("The equation no sultion")
    elif delta == 0:
        x = -b/(2*a)
        print(f"{a}*({x}**2) + {b}*({x}) + {c} = 0")
    else:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        print(f"X1 = {x1}, X2 = {x2}  ")
