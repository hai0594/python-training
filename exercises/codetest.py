def zero_fuel(distance_to_pump, mpg, fuel_left):
    fomula = distance_to_pump/(mpg * fuel_left)
    if fomula <= 1:
        return True
    else:
        return False

print(zero_fuel(63, 13, 1))