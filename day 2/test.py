def check_data_type(input):
    try:
        x = int(input)
        print("integer", x)
    except ValueError:
        try:
            x = float(input)
            print("float", x)
        except ValueError:
            if input.lower() == 'true' or input.lower() == 'false':
                x = bool(input)
                print("boolen")
            else:
                print("string")


Enter1 = input("Enter something:")
check_data_type(Enter1)
