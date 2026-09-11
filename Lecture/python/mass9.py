#10. take input of three values and shown the greter value 

a= int(input("Enter Value a : "))
b= int(input("Enter Value b : "))
c= int(input("Enter Value c : "))

if a >= b:
    print("A: ", a)
elif b >= c:
    print("B:", b)
elif c >= a:
    print("C:",c)