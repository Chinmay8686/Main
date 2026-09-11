#5. Take input from the user and use match case statement  
day = int(input("Enter the Day NUmber:"))

match day:
    case 1:
       print("Monday")
    case 2:
       print("Tuesday")
    case _:
       print("Santa")