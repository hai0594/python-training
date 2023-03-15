# Nhập vào một năm bất kỳ. Kiểm tra xem năm đó có phải là năm nhuận hay không ?
y = int(input("Enter any year to check: "))
if y % 100 == 0 and y % 400 == 0:
    print("Nam Nhuan")
elif y % 4 == 0:
    print("Nam Nhuan")
else:
    print("Nam Thuong")
