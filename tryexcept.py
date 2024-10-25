import math #need to import math from the get go
def add (num1,num2): 
    return num1 + num2
def subtract(num1,num2): 
    return num1 - num2
def multiply(num1,num2): 
    return num1 * num2
def divide (num1,num2):
    if num2 !=0:
        return num1/num2 
    else:
        return "Error ! Division by zero!"#need this to account for zero conundrum
def exponent(num1,num2):
    return num1 ** num2
def modulus(num1,num2):
    return num1 % num2
def sqaurert(num1):
    return math.sqrt(num1)

def super_calculator():
    while True:
        print("Which operation would you like?") #Lets user know they can pick from the below
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divison")
        print("5. Exponent")
        print("6. Modulus")
        print("7. Square Root")
        print("8. Exit")

        choice = input("Enter Choice ")
#These if statements call the functions
#Each choice needs to have the input() within to account for each task and number
#After each operation is complete the code will restart fresh unless the user decides to quit
#Added the try and except methods to catch user errors. This will restart the program
        if choice == '8':
            print("Exiting, thank you!")
            break
        elif choice == '1':
            print("You picked Add")
            try:
                num1 = float(input("Enter your first number: "))
                num2 = float(input("Enter your second number: "))
                print(f"{num1} + {num2} = {add(num1, num2)}")
            except ValueError:
                print("Invalid input! Please enter valid numbers.")
        elif choice == '2':
            print("You picked Subtract")
            try:
                num1 = float(input("Enter your first number: "))
                num2 = float(input("Enter your second number: "))
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            except ValueError:
                print("Invalid input! Please enter valid numbers.")
        elif choice == '3':
            print("You picked Multiply")
            try:
                num1 = float(input("Enter your first number: "))
                num2 = float(input("Enter your second number: "))
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            except ValueError:
                print("Invalid input! Please enter valid numbers.")
        elif choice == '4':
            print("You picked Divide")
            try:
                num1 = float(input("Enter your first number: "))
                num2 = float(input("Enter your second number: "))
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            except ValueError:
                print("Invalid input! Please enter valid numbers.")
        elif choice == '5':
            print("You picked Exponent")
            try:
                num1 = float(input("Enter your first number: "))
                num2 = float(input("Enter your second number: "))
                print(f"{num1} to the power of {num2} is {exponent(num1, num2)}")
            except ValueError:
                print("Invalid input! Please enter valid numbers.")
        elif choice == '6':
            print("You picked Modulus")
            try:
                num1 = float(input("Enter your first number: "))
                num2 = float(input("Enter your second number: "))
                print(f"{num1} % {num2} leaves {modulus(num1, num2)} left")
            except ValueError:
                print("Invalid input! Please enter valid numbers.")
        elif choice == "7":
            print("You picked Square Root")
            try:
                num1 = float(input("Enter your number: "))
                print(f"The square root of {num1} is {square_root(num1)}")
            except ValueError:
                print("Invalid input! Please enter a valid number.")
        else:
            print("Invalid Input! Please try again.")

if __name__ == "__main__":
    super_calculator()