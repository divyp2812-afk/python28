print("Welcome to the Student Data Organizer!")

students = []

while True:
    print("\n1. Add Student")
    print("2. Display all students")
    print("3. Update student information")
    print("4. Delete student")
    print("5. Display subjects offered")
    print("6. Exit")

    
    choice = int(input("Choose a number: "))

    if choice == 1:
        student_id = input("Enter Student ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        grade = input("Enter Grade: ")
        dob = input("Enter Date of Birth: ")
        subjects = input("Enter Subjects: ")

        student = [student_id, name, age, grade, dob, subjects]
        students.append(student)
        print("stutent added successfully!")

    elif choice == 2:
        if not students:
            print("No student records found.")
        else:
            print("\n--- Student Records ---")
            for s in students:
                print("ID:", s[0])
                print("Name:", s[1])
                print("Age:", s[2])
                print("Grade:", s[3])
                print("DOB:", s[4])
                print("Subjects:", s[5])

    elif choice == 3:
        student_id = input("Enter student ID to update: ")
        found = False
        for s in students:
            if s[0] == student_id:
                s[1] = input("Enter new name: ")
                s[2] = input("Enter new age: ")
                s[3] = input("Enter new grade: ")
                s[4] = input("Enter new date of birth: ")
                s[5] = input("Enter new subjects (comma-separated): ").split(",")
                print("student updated!")
                found = True
                break
        if not found:
            print("Student not found.")

    elif choice == 4:
        student_id = input("Enter student ID to delete: ")
        found = False
        for s in students:
            if s[0] == student_id:
                students.remove(s)
                print(" Student deleted!")
                found = True
                break
        if not found:
            print("Student not found.")

    elif choice == 5:
        print("\n--- Subjects Offered ---")
        subject = set()
        for s in students:
            subject.add(s[5])
        print(", ".join(subject) if subject else "No subject available.")

    elif choice == 6:
        print(" Exiting program...")
        break

    else:
        print("Invalid choice. Try again!")