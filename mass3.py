#4. Enter youtr age if age is greater tan 18 then print entry Allowed
age = int(input("Enter Age:"))
has_id = True
if age >= 18:
    if has_id:
        print("Entry Allowed")
    else:
        print("Id Required")
else:
    print("Underage")
