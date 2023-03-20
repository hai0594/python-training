# Đếm số chẵn và lẻ trong đoạn [0, 1000] theo 2 cách: thông thường và list comprehension
# thông thường
count_even = 0
count_odd = 0
for n in range(1000):
    if n % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
print(f'Even : {count_even}\nOdd : {count_odd}')

# list comprehension
Even = [even for even in list(range(1000)) if even % 2 == 0]
print("Even:",len(Even))

Odd = [odd for odd in list(range(1000)) if odd % 2 != 0]
print("Odd:",len(Odd))

Numbers = ["Even" if even % 2 == 0 else "Odd" for even in list(range(1000))]
print(f"Even number: {Numbers.count('Even')}")
print(f"Odd number: {Numbers.count('Odd')}")