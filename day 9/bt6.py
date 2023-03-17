# Nhập vào một số nguyên dương n. Đếm số lượng số chẵn và lẻ trong đoạn [0, n]

n = int(input("Enter number:"))
even = []
odd = []
while n <= 0:
    print(f"{n} is negative number")
    n = int(input("Enter number:"))
for count in range(0,n):
    if count % 2 == 0:
        even.append(count)
    else:
        odd.append(count)
print(f"Even :{(len(even))}")
print(f"Odd  :{(len(odd))}")
