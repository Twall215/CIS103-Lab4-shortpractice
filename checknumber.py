def check_number(num):
    if num > 0:#if the number is greater than zero
        return f"{num} is positive."
    elif num < 0:#if the number is less than zero
        return f"{num} is negative."
    else:#If its anything else then its gotta be zero
        return f"{num} is zero."
number = float(input("Entger a number "))#Ensures the users put in a number

result = check_number(number)
print(result)
