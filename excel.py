my_dict = {"apple": 1, "banana": 2, "cherry": 3}

user_input = input("Enter a key: ")

if user_input in my_dict:
    remaining_data = my_dict[user_input]
    print(remaining_data)
else:
    print("Key not found")