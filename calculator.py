#write a calculator program that hasa menu system where it ask for a choise from the user (+, -, *, /, !(factorial)). it should display the out until the user explicitly terminated te proram by writing exit 
while True:
    print("\n----- CALCULATOR -----")
    print("+ : Addition")
    print("- : Subtraction")
    print("* : Multiplication")
    print("/ : Division")
    print("! : Factorial")
    print("exit : Exit")

    choice = input("Enter your choice: ")

    if choice == "exit":
        print("Program terminated.")
        break

    elif choice == "+":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Result =", a + b)

    elif choice == "-":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Result =", a - b)

    elif choice == "*":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Result =", a * b)

    elif choice == "/":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        if b == 0:
            print("Cannot divide by zero")
        else:
            print("Result =", a / b)

    elif choice == "!":
        n = int(input("Enter a number: "))

        factorial = 1
        i = 1

        while i <= n:
            factorial = factorial * i
            i = i + 1

        print("Factorial =", factorial)

    else:
        print("Invalid choice!")