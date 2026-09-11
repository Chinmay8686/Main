#10. take input of three values and shown the greter value 

a= int(input("Enter Value a : "))
b= int(input("Enter Value b : "))
c= int(input("Enter Value c : "))

if a > b and a >c:
    print("A: ", a)
elif b > c and b > a:
    print("B:", b)
elif c > a and c > b:
    print("C:",c)
elif a == b and  a == c:
   print("All Values Are Equal")
elif a == b and b > c:
    print("A and B are Greater")
elif b == c and a > c:
    print("B and C are Greater")  
elif a == c and c > b:
    print("A and C are Greater")
  