# Giải và biện luận phương trình bậc nhất một ẩn ax + b = 0 (ẩn x, a và b là hai số cho trước)
print("Equation: ax + b = 0")
a = int(input("a number:"))
b = int(input("b number:"))
if a == 0:
    if b == 0:
        print("The euqation satisfied all value:")
    else:
        print("The equation no soluion")
else:
    x = -b/a
    print(f"{a}x + {b} = 0\nx = {-b}\{a}\nx = {x}")
