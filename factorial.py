#define the function and print 
n = int(input("Enter the Number:"))
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else: 
        return n * factorial(n-1)
print("Factorial of", n, "is:", n*(n-1)*(n-2)*(n-3))
