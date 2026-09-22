#create a basic calculator used for addition or substraction
# Basic calculator for addition, subtraction, division and multiplication

a = int(input("Enter Value of A: "))
b = int(input("Enter Value of B: "))
c = int(input("Method (1-4): "))

add = a + b
sub = a - b
div = a / b
mul = a * b

match c:
    case 1:
        print("Addition is:", add)

    case 2:
        print("Subtraction is:", sub)

    case 3:
        print("Division is:", div)

    case 4:
        print("Multiplication is:", mul)

    case _:
        print("Invalid Method! Please enter 1, 2, 3 or 4.") 