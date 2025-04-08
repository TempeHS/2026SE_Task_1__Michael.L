import sys

start = input("Login, Register, or Quit: ")

while start == "Login" or "Register" or "Quit":
    if not start == "Login" or "Register" or "Quit":
        start = input("Login, Register, or Quit: ")



def login():
    while True:
        username = input("What is your username: ")
        password = input("What is your password: ")
        with open("plain_text.txt", "r") as file:
            for line in file:
                row = line.split(",")
                check_username = row[0]
                check_password = row[1]
                if username in check_username and password in check_password:
                    print("Logged in successfuly!")
                    change_password()
                elif username not in check_username or password not in check_password:
                    print("Incorrect username or passwword")

        # if check_username == username and check_password == password:
        #     print("Login Successul!")
        # else:
        #     print("Username or password incorrect")

def Register():
    global new_password
    new_username = input("New username: ")
    new_password = input("New password: ")
    with open("plain_text.txt", "a") as file:
        file.write(f"\n{new_username},{new_password}")
    print(f"{new_username} has been registered!")
    start2 = input("Login or Quit: ")
    if start2 == "Login":
        login()
    elif start2 == "Quit":
        print("Goobye!")
        sys.exit(1)


def change_password():
    start3 = input("Change password or Quit: ")
    if start3 == "Quit":
        print("Goodbye!")
        sys.exit(1)
    elif start3 == "Change password":
        newest_password = input("New password: ")
        with open("plain_text.txt", "a") as file:
            for line in file:
                line.replace(new_password, newest_password)

if start == "Login":
    login()
elif start == "Register":
    Register()
elif start == "Quit":
    print("Goodbye")
    sys.exit(1)