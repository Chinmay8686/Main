#8. take marks input and Assign grade as per marks 

Marks = int(input("Enter Marks: "))

if Marks >= 90 and Marks <= 100:
    print("Grade is OUTSTANDING ")
elif Marks >= 80:
    print("Grade is A ")
elif Marks >= 65:
    print("Grade is B")
elif Marks >= 35:
    print("Grade is C")
elif Marks >= 0:
    print("Grade is F")