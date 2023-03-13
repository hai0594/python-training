#set
art_students = {"John", "Max", "Anna", "Bob", "Obito"}
math_students = {"Max", "Mery", "David", "Anna", "Naruto", "John"}
#Tìm những người bạn học cả vẽ lẫn toán
art_math_class = art_students.intersection(math_students)
print (art_math_class)
#Tìm những người bạn học vẽ nhưng không học toán
art_class = art_students.difference(math_students)
print(art_class)
#Tìm những người bạn học toán nhưng không học vẽ
math_class = math_students.difference(art_students)
print(math_class)
#Tìm những người bạn học vẽ hay toán không phải cả hai
math_or_art = art_students.symmetric_difference(math_students)
print(math_or_art)
#Tìm tất cả những người bạn
map_art_math = art_students.union(math_students)
print(art_students | math_students)
print(map_art_math)