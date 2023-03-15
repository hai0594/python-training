# Nhập hai số a và b từ bàn phím. In ra số lớn nhất và nhỏ nhất trong hai số

a = eval(input("Enter number a:"))
b = eval(input("Enter number b:"))
if a > b:
    print(f"Max: {a}")
    print(f"Min: {b}")
elif a == b:
    print(f"{a} equal {b}")
else:
    print(f"Min: {a}")
    print(f"Max: {b}")