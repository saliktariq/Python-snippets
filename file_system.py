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
