class Node:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def path(self):
        if self.parent:
            return self.parent.path() + '/' + self.name
        return self.name

class File(Node):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return self.name

class Folder(Node):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return self.name

def find_child(name, parent):
    for child in parent.children:
        if child.name == name:
            return child
    return None

def make_dir(name, parent):
    if find_child(name, parent) is not None:
        print(f"Directory {name} already exists in the current directory")
        return
    folder = Folder(name)
    parent.add_child(folder)
    print(f"New directory {name} created")

def make_file(name, parent):
    if find_child(name, parent) is not None:
        print(f"File {name} already exists in the current directory")
        return
    file = File(name)
    parent.add_child(file)
    print(f"New file {name} created")

root = Folder("root")
current_dir = root

def print_path(node):
    print(node.path(), end='')

def parse_command(line):
    global current_dir
    parts = line.split()
    if not parts:
        return
    command, *args = parts

    if command == 'cd':
        if not args:
            return
        name = args[0]
        if name == '..' and current_dir.parent:
            current_dir = current_dir.parent
        else:
            folder = find_child(name, current_dir)
            if isinstance(folder, Folder):
                current_dir = folder
            else:
                print(f"No subdirectory {name} found")
    elif command == 'cdr':
        current_dir = root
    elif command == 'jump':
        if not args:
            return
        name = args[0]
        folder = find_child(name, root)
        if isinstance(folder, Folder):
            current_dir = folder
        else:
            print(f"No directory {name} found")
    elif command == 'ls':
        for child in current_dir.children:
            print(child, end='\t')
        print()
    elif command == 'mkdir':
        if not args:
            return
        name = args[0]
        make_dir(name, current_dir)
    elif command == 'mkfile':
        if not args:
            return
        name = args[0]
        make_file(name, current_dir)
    else:
        print(f"Invalid command {command}")
        

# Define the file system tree
root = Folder("root")
current_dir = root

# Add top-level folders
programming_folder = Folder("Programming")
root.add_child(programming_folder)
music_folder = Folder("Music")
root.add_child(music_folder)

# Add subfolders and files within the "Programming" folder
python_folder = Folder("Python")
programming_folder.add_child(python_folder)
make_file("script.py", python_folder)
make_file("README.md", python_folder)

java_folder = Folder("Java")
programming_folder.add_child(java_folder)
make_file("Main.java", java_folder)
make_file("README.md", java_folder)

# Add subfolders and files within the "Music" folder
rock_folder = Folder("Rock")
music_folder.add_child(rock_folder)
make_file("Stairway to Heaven.mp3", rock_folder)
make_file("Hotel California.mp3", rock_folder)

jazz_folder = Folder("Jazz")
music_folder.add_child(jazz_folder)
make_file("Take Five.mp3", jazz_folder)
make_file("My Favorite Things.mp3", jazz_folder)

# Display the file system structure
print_path(root)
print()
parse_command("ls")

# Query the file system
parse_command("cd Music")
print_path(current_dir)
print()
parse_command("ls")

parse_command("cd Jazz")
print_path(current_dir)
print()
parse_command("ls")

parse_command("jump Programming")
print_path(current_dir)
print()
parse_command("ls")

parse_command("mkfile script.py")
parse_command("mkfile README.md")

parse_command("cd Python")
print_path(current_dir)
print()
parse_command("ls")

parse_command("cd ..")
print_path(current_dir)
print()
parse_command("ls")

parse_command("cd ..")
print_path(current_dir)
print()
parse_command("ls")

parse_command("cdr")
print_path(current_dir)
print()
parse_command("ls")

