""" def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split()) """

""" def to_jaden_case(string):
    cap_string = " ".join(word.capitalize() for word in string.split())
    return cap_string """

""" def find_smallest_int(arr):
    min_int = "".join(str(small) for small in arr  )
    return  min_int
print(find_smallest_int([34, 15, 88, 2]))
 """
""" import math
def litres(time):
    lit = math.floor(time/2)
    return lit
print(litres(3)) """
def solution(text, ending):
    return text.endswith(ending[-2:])
print(solution("abc","abcd" ))

print("Ending"[-2:])