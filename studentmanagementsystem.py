# Student Management System

students = {}

def add_student():
    roll = input("Enter Roll Number: ")

    if roll in students:
        print("Student with this Roll Number already exists!")
        return

    name = input("Enter Student Name: ")
    age = input("Enter Age: ")
    branch = input("Enter Branch: ")
    marks = input("Enter Marks: ")

    students[roll] = {
        "Name": name,
        "Age": age,
        "Branch": branch,
        "Marks": marks
    }

    print("Student Added Successfully!\n")


def view_students():
    if not students:
        print("No Student Records Found.\n")
        return

    print("\n----- Student Records -----")
    for roll, details in students.items():
        print(f"""
Roll Number : {roll}
Name        : {details['Name']}
Age         : {details['Age']}
Branch      : {details['Branch']}
Marks       : {details['Marks']}
------------------------------""")
    print()


def search_student():
    roll = input("Enter Roll Number to Search: ")

    if roll in students:
        s = students[roll]
        print("\nStudent Found")
        print("Roll Number :", roll)
        print("Name        :", s["Name"])
        print("Age         :", s["Age"])
        print("Branch      :", s["Branch"])
        print("Marks       :", s["Marks"])
    else:
        print("Student Not Found.")
    print()


def update_student():
    roll = input("Enter Roll Number to Update: ")

    if roll in students:
        print("Enter New Details")
        students[roll]["Name"] = input("Name: ")
        students[roll]["Age"] = input("Age: ")
        students[roll]["Branch"] = input("Branch: ")
        students[roll]["Marks"] = input("Marks: ")

        print("Student Updated Successfully!\n")
    else:
        print("Student Not Found.\n")


def delete_student():
    roll = input("Enter Roll Number to Delete: ")

    if roll in students:
        del students[roll]
        print("Student Deleted Successfully!\n")
    else:
        print("Student Not Found.\n")


while True:
    print("===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Thank You!")
        break
    else:
        print("Invalid Choice! Please Try Again.\n")
