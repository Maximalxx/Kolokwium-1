def display_positive_integers(n):
    if n >= 0:
        for number in range(n+1):
            print(number)
    else:
        print("integer is not positive")

# display_positive_integers(5)
# display_positive_integers(0)
# display_positive_integers(-3)