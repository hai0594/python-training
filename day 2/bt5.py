def check_data_type(input):
    try:
        # check integer
        x = int(input)
        print("Data type is integer, Number:", x)
    except ValueError:
        try:
            # check float
            x = float(input)
            print("Data type is float, Number:", x)
        except ValueError:
            # check bool
            if input.lower() == "true" or input.lower() == "false":
                x = bool(input)
                print("Data type is boolean")
            else:
                print("Data type is string")


Enter1 = input("Enter something:")
check_data_type(Enter1)
Enter2 = input("Enter something:")
check_data_type(Enter2)
Enter3 = input("Enter something:")
check_data_type(Enter3)
Enter4 = input("Enter something:")
check_data_type(Enter4)
