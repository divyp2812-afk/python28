print("Employee Management System using OOP and while True loop")

class person:
    def __init__(self):
        self.name = ""
        self.age = 0

    def create_person(self):
        self.name = input("Enter name:")
        self.age = int(input("Enter age:"))

    def show(self):
        print(f"Name: {self.name},Age: {self.age}")

class employee(person):
    def __init__(self):
        super().__init__()
        self.emp_id = 0
        self.salary = 0

    def create_employee(self):
        self.create_person()
        self.emp_id = int(input("Enter employee ID : "))
        self.salary = float(input("Enter Salary:"))

    def show(self):
        print(f"Name: {self.name},Avg : {self.age}, Id: {self.emp_id}, Salary:{self.salary}")

class Manger(employee):
    def __init__(self):
        super().__init__()
        self.department = ""

    def create_manger(self):
        self.create_employee()
        self.department = input("Enter Department:")

    def show(self):
        print(f"Name:{self.name},Age: {self.age}, ID: {self.emp_id}, salary: {self.salary}, Dept: {self.department}")

        
        

Person = person()
Employee = employee()
manager = Manger()

while True:
    print("\nChoose an operation:")
    print("1. Create a person")
    print("2. Create a Employee")
    print("3. Creat a Manger")
    print("4. Show Details")
    print("5. Exit")


    choice = input("Enter your choice: ")

    if choice == "1":
        Person.create_person()
        print("Employee created!")

    elif choice == "2":
        Employee.create_employee()
        print("Employee Created!")

    elif choice == "3":
        manager.create_manger()
        print("Manger created!")

    elif choice == "4":
        print("\n--Details--")
        Person.show()
        Employee.show()
        manager.show()

    elif choice == "5" :
        print("Exiting the system. All resources have been freed.")
        print("Good Bye!")
        break    

    else:
        print("Invalid choice! Try again.")