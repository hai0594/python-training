# Creating a list of numbers, then multiplying each number by 2.
# Creating the list
list_number = []
times = 0
int_list = []
while times < 5:
    number = input("Add number to list:")
    list_number.append(number)
    times += 1
print(list_number)
# Convert string list to int list
for val in list_number:
    int_list.append(int(val))
print(int_list)
# Use comprehension to multi each number in list by 2
x2 = [x*2 for x in int_list]
print(x2)
