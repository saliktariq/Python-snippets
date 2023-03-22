import os


def sign_up(username, password):
    file_path = "user.dat"
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                if line.strip().split(":")[0] == username:
                    print("Username already exists.")
                    return False
    with open(file_path, "a") as file:
        file.write(f"{username}:{password}\n")
    print("User created.")
    return True


def login(username, password):
    file_path = "user.dat"
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                stored_username, stored_password = line.strip().split(":")
                if stored_username == username and stored_password == password:
                    print("Login successfully.")
                    return True
    print("Wrong login.")
    return False


def forget_password(username):
    file_path = "user.dat"
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                stored_username, stored_password = line.strip().split(":")
                if stored_username == username:
                    new_password = input("Enter new password: ")
                    lines[i] = f"{username}:{new_password}\n"
                    with open(file_path, "w") as file:
                        file.writelines(lines)
                    print("Password changed successfully.")
                    return True
    print("Username not found.")
    return False
