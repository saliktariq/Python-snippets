from modules import admin, user

while True:
    print("1. Create user")
    print("2. Login")
    print("3. Forget password")
    print("4. Create admin")
    print("5. Login admin")
    print("6. Forget password admin")
    print("7. Create catalogue")
    print("8. View catalogue")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        user.sign_up(username, password)
    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        user.login(username, password)

    elif choice == "3":
        username = input("Enter username: ")
        user.forget_password(username)
    elif choice == "4":
        username = input("Enter username: ")
        password = input("Enter password: ")
        admin.sign_up(username, password)
    elif choice == "5":
        username = input("Enter username: ")
        password = input("Enter password: ")
        admin.login(username, password)
    elif choice == "6":
        username = input("Enter username: ")
        admin.forget_password(username)
    elif choice == "7":
        id = input("Enter ID: ")
        name = input("Enter Name: ")
        description = input("Enter Description: ")
        admin.create_catalogue(id, name, description)
    elif choice == "8":
        admin.display_catalogue()
    elif choice == "0":
        break
    else:
        print("Invalid choice. Please try again.")
