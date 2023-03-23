import os

class FileSystem:
    def __init__(self):
        self.current_directory = "/"
        self.root = {}

    def mkdir(self, path):
        directories = path.split("/")
        current = self.root
        for directory in directories:
            if directory not in current:
                current[directory] = {}
            current = current[directory]

    def cd(self, path):
        if path == "/":
            self.current_directory = path
            return
        directories = path.split("/")
        current = self.root
        for directory in directories:
            if directory not in current:
                print("Directory not found")
                return
            current = current[directory]
        self.current_directory = path

    def ls(self):
        current = self.root
        if self.current_directory != "/":
            directories = self.current_directory.split("/")
            for directory in directories:
                if directory not in current:
                    return
                current = current[directory]
        for name, value in current.items():
            if isinstance(value, dict):
                print(f"{name}/")
            else:
                print(name)

    def touch(self, path):
        directories = path.split("/")
        current = self.root
        for directory in directories[:-1]:
            if directory not in current:
                print("Directory not found")
                return
            current = current[directory]
        current[directories[-1]] = ""

    def rm(self, path):
        directories = path.split("/")
        current = self.root
        for directory in directories[:-1]:
            if directory not in current:
                print("Directory not found")
                return
            current = current[directory]
        if directories[-1] not in current:
            print("File not found")
            return
        del current[directories[-1]]

if __name__ == "__main__":
    fs = FileSystem()

    while True:
        command = input(fs.current_directory + "> ")
        parts = command.split(" ")

        if parts[0] == "mkdir":
            fs.mkdir(parts[1])
        elif parts[0] == "cd":
            fs.cd(parts[1])
        elif parts[0] == "ls":
            fs.ls()
        elif parts[0] == "touch":
            fs.touch(parts[1])
        elif parts[0] == "rm":
            fs.rm(parts[1])
        elif parts[0] == "dir":
            fs.ls()  # Same as ls command
        elif parts[0] == "exit":
            break
        else:
            print("Command not found")
