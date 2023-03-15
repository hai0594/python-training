# Nhập vào một số nguyên dương n tính tổng các chữ số của n. Ví dụ: n = 4312 => S = 4 + 3 + 1 + 2 = 10
n = input("Enter number:")
total = 0

for amount in n:
    total += int(amount)
print(total)
