# Initialising dictionary
student_grade = {}

# Add a new student
def add_student(name, grade):
    student_grade[name] = grade
    print(f"Added {name} with a {grade}")

# Update a student
def update_student(name, grade):
    if name in student_grade:
        student_grade[name] = grade
        print(f"Updated {name} with a {grade}")
    else:
        print(f"Student {name} not found")

# Delete a student
def delete_student(name):
    if name in student_grade:
        del student_grade[name]
        print(f"Deleted {name}")
    else:
        print(f"Student {name} not found")

# View all students
def view_all_students():
    if student_grade:
        for name, grade in student_grade.items():
            print(f"{name} - {grade}")
    else:
        print("No students in the list")

def main():
    while True:
        print('\n Student Grades Management System')
        print('1. Add a student')
        print('2. Update a student')
        print('3. Delete a student')
        print('4. View all students')
        print('5. Exit')

        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = input("Enter student name: ")
            grade = input("Enter student grade: ")
            add_student(name, grade)
        elif choice == 2:
            name = input("Enter student name: ")
            grade = int(input("Enter student grade: "))
            update_student(name, grade)
        elif choice == 3:
            name = input("Enter student name: ")
            delete_student(name)
        elif choice == 4:
            view_all_students()
        elif choice == 5:
            print("Thank you for using the Student Grades Management System")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()