def analyze_numbers(a, b):
    if a > b:
        return 5
    elif a % 2 == 0:
        if b % 2 == 0:
            return 2
        else:
            return 8
    else:
        return 9

print(analyze_numbers(44,1))
print(analyze_numbers(4, 6))
print(analyze_numbers(4, 5))
print(analyze_numbers(5, 6))
