def check_number(num):
    if num > 0:
        return f"{num} is positive."
    elif num < 0:
        return f"{num} is negative."
    else:
        return f"{num} is zero."
number = float(input("Entger a number "))

result = check_number(number)
print(result)
