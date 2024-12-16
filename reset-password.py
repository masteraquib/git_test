username = input("Enter username = ")
password = input("Enter password = ")
is_auth = False
if username == 'admin' and password == "admin":
    print("You can reset")
    is_auth =  True
else:
    print("You cannot reset")


if is_auth:
    print("Now Reset")
