username = "python"
password = "rules"
a = 0

while a < 5:
    user = input("Enter username: ")
    passw = input("Enter password: ")

    if user == username and passw == password:
        print("Welcome !")
        break
    else:
        print("Invalid username or password. Enter again.")
        a += 1

if a == 5:
    print("Access denied.")
