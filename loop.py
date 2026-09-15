#loop 
correct_pass="some_pass"
not_found = True

while not_found:
    string = input("Enter a String: ")
    if string == correct_pass: 
      not_found = False 
    else:
     print("Wrong password try again!! ")
     
print("Password Matched! ")

