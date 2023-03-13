# Create list
students = [["SV001", "Bob", 23], [
    "SV002", "Kenny", 34], ["SV003", "Henry", 45]]

# Lấy ra thông tin của sinh viên thứ nhất và in ra định dạng "ID: {id}, name: {name} - age: {age}"
# Get info 0 position
position0 = students[0]
print(position0)

# Get list info
list0_0 = position0[0]
list0_1 = position0[1]
list0_2 = position0[2]

# Format student information
print(f'ID: {list0_0}, name: {list0_1} - age: {list0_2}')

# Lấy ra tuổi của sinh viên thứ hai
age2 = students[2][2]
print("Age:", age2)

# Lấy ra thông tin hai sinh viên cuối cùng
last = students[-1]
nlast = students[-2]
print(f"Last students: {last}, Near last:{nlast}")

# Lấy ra id của sinh viên thứ ba
id3 = students[2][0]
print("ID:", id3)
