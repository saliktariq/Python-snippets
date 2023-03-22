import os
import datetime


def sign_up(username, password):
    file_path = "admin.dat"
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                if line.strip().split(":")[0] == username:
                    print("Admin user already exists.")
                    return False
    with open(file_path, "a") as file:
        file.write(f"{username}:{password}\n")
    print("Admin created.")
    return True


def login(username, password):
    file_path = "admin.dat"
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                stored_username, stored_password = line.strip().split(":")
                if stored_username == username and stored_password == password:
                    print("Admin login successfully.")
                    return True
    print("Wrong login details.")
    return False


def forget_password(username):
    file_path = "admin.dat"
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
    print("Admin not found.")
    return False


def create_catalogue(id, name, description):
    file_path = "catalogue.dat"
    timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    with open(file_path, "a") as file:
        file.write(f"{timestamp} ID:{id} Name:{name} Description:{description}\n")
    print("Catalogue created successfully.")


def display_catalogue():
    file_path = "catalogue.dat"
    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())
