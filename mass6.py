#7. take input from user if age is under or equal to 12 ten discount applied
age = int(input("Enter Age: "))
ticket_price = 100 
if age <= 12:
    ticket_price *= 0.9
else:
   print("ticket_price:", ticket_price)
