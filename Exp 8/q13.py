while True:
    password = input("Enter password: ")
    if password == "Secret":
        print("Access granted")
        break
    else:
        print("Your password is incorrect")
