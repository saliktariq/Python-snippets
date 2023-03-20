master_list = []  # initialize master list to store all records


# function to calculate total and average marks
def calculate_marks(marks):  # argument 'marks' is of type list
    total = sum(marks)
    average = total / len(marks)
    return total, average


# function to check if roll number already exists
def check_roll_number(roll_number):  # argument 'roll_number' is of type int
    for record in master_list:
        if record[1] == roll_number:  # record[1] is roll number
            return True
    return False


# function to create a new record
def create_record():
    # get inputs from user
    name = input("Enter name: ")
    while True:
        roll_number = input("Enter roll number: ")
        if check_roll_number(roll_number):
            print("Roll number already exists, please choose another.")
        else:
            break
    marks = []  # Empty list to contain all marks
    for i in range(3):
        marks.append(int(input(f"Enter mark {i + 1}: ")))
    # calculate total and average marks
    total, average = calculate_marks(marks)  # simultaneous assignment of total and average from returned values
    # create a list to store record data
    record = [name, roll_number, marks, total, average]
    # add record to master list
    master_list.append(record)
    print("Record created successfully.")


# function to search for a record by roll number
def search_record():
    roll_number = input("Enter roll number to search: ")
    for record in master_list:
        if record[1] == roll_number:
            print(f"Record found: {record}")
            return
    print("Record not found.")


# function to update a record by roll number
def update_record():
    roll_number = input("Enter roll number to update: ")
    for record in master_list:
        if record[1] == roll_number:
            # get new inputs from user
            record[0] = input(f"Enter new name ({record[0]}): ") or record[0]
            marks = []
            for i in range(3):
                marks.append(int(input(f"Enter new mark {i + 1} ({record[2][i]}): ")) or record[2][i])
            # calculate total and average marks
            total, average = calculate_marks(marks)
            record[2] = marks
            record[3] = total
            record[4] = average
            print("Record updated successfully.")
            return
    print("Record not found.")


# function to delete a record by roll number
def delete_record():
    roll_number = input("Enter roll number to delete: ")
    for record in master_list:
        if record[1] == roll_number:
            master_list.remove(record)
            print("Record deleted successfully.")
            return
    print("Record not found.")


# function to display a record by roll number
def display_record():
    roll_number = input("Enter roll number to display: ")
    for record in master_list:
        if record[1] == roll_number:
            print(record)
            return
    print("Record not found.")


# function to display all records
def display_all_records():
    if len(master_list) == 0:
        print("No records")
    else:

        for record in master_list:
            print(record)


# display menu
while True:
    print("""
    Menu:
    1. Create new record
    2. Search record
    3. Update record
    4. Delete record
    5. Display record
    6. Display all records
    7. Exit
    """)
    choice = input("Enter your choice: ")
    if choice == "1":
        create_record()
    elif choice == "2":
        search_record()
    elif choice == "3":
        update_record()
    elif choice == "4":
        delete_record()
    elif choice == "5":
        display_record()
    elif choice == "6":
        display_all_records()
    elif choice == "7":
        break
    else:
        print("Invalid choice! ")
