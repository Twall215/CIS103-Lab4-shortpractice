def Sumitup(num1,num2):
    if (num1 or num2) != (int(num1) or int(num2)):#Error checking
        print("Please use only numbers")
    else:
        total = int(num1) + int(num2)#Add em all up
        print(f"{num1} + {num2} = {total}")
    
  #calls the function  
Sumitup(1,2)
