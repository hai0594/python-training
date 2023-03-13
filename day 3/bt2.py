'a' > 'b'
# false bởi vì a có giá trị là 97 còn b là 98
3.0 > 3
# false bới vì 3.0 cũng bằng 3
3 and 4 or 0
# true độ ưu tiên sẽ là and rồi đến or, 3 and 4 > true, 0 or 4 true nên sẽ là true
'a' or '1'
"""
trong toán tử or sẽ sét giá trị đầu tiên bên trái trước
a là true nên theo qui tắc đối số sẽ trả về giá trị là a
"""
not None
# True bởi vì trong kiểu boolean thì 0, None, Rỗng sẽ là false, ngược lại với false là true
not 0
# True tương đương với None
