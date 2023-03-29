def binary_array_to_number(arr):
    binary_string = "".join(str(bit) for bit in arr)
    int_value = int(binary_string,2)
    return int_value
print(binary_array_to_number([0, 0, 0, 1]))

