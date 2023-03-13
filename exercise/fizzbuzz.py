lst = list(range(1,1000))
for number in lst:
    user_input = input("Enter number: ")
    if user_input.isdigit():
        number = int(user_input)
        if 0 < number <= 101:
            if number % 3 == 0:
                if number % 5 == 0:
                    print("Fizz Buzz")
                else:
                    print("Fizz")

            elif number % 5  ==0:
                print("Buzz")

            else:
                print(number)
        else:
            print("Out of range")
    else:
        print("Wrong format")
        