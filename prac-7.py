print('==================================')
print("Welcome to Multi-Utility Toolkit")
print('==================================')
print("Choose an option:")

import datetime
import time
import math
import random
import uuid

while True:
    print("1. Date/Time and Time Operations")
    print("2. Mathematical Operations")
    print("3. Random Data Generation")
    print("4. Generate Unique Identifiers (UUID)")
    print("5. File Operations")
    print("6. Explore Module Attributes")
    print("7. Exit")

    main_choice = input("Enter your choice: ")

    if main_choice == "1":
        while True:
            print("\n--- Date/Time Operations ---")
            print("1. Display current date and time")
            print("2. Calculate difference between two date/times")
            print("3. Format date into custom format")
            print("4. Stopwatch")
            print("5. Countdown Timer")
            print("6. Back to main menu")

            dt_choice = input("Enter your choice: ")

            if dt_choice == "1":
                now = datetime.datetime.now()
                print("Current Date & Time:", now.strftime("%Y-%m-%d %H:%M:%S"))

            elif dt_choice == "2":
                d1 = input("Enter first date (YYYY-MM-DD): ")
                d2 = input("Enter second date (YYYY-MM-DD): ")
                try:
                    date1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
                    date2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
                    diff = abs((date2 - date1).days)
                    print("Difference =", diff, "days")
                except:
                    print("Invalid date format!")

            elif dt_choice == "3":
                d = input("Enter date (YYYY-MM-DD): ")
                try:
                    date_obj = datetime.datetime.strptime(d, "%Y-%m-%d")
                    print("Formatted:", date_obj.strftime("%d %B, %Y"))
                except:
                    print("Invalid date format!")

            elif dt_choice == "4":
                input("Press Enter to start stopwatch...")
                start = time.time()
                input("Press Enter to stop stopwatch...")
                end = time.time()
                print("Elapsed time:", round(end - start, 2), "seconds")

            elif dt_choice == "5":
                try:
                    seconds = int(input("Enter countdown time in seconds:"))
                    for i in range(seconds, 0, -1):
                        print(i)
                        time.sleep(1)
                    print("Time's up!")
                except:
                    print("Invalid choice!")

            elif dt_choice == "6":
                break

            else:
                print("Invalid choice!")

    elif main_choice == "2":
        while True:
            print("\n--- Mathematical Operations ---")
            print("1. Calculate Factorial")
            print("2. Solve compound interest")
            print("3. Trignometric Calculations")
            print("4. Area of geometric shapes")
            print("5. Back to main menu")

            math_choice = input("Enter your choice: ")

            if math_choice == "1":
                try:
                    num = int(input("Enter a number: "))
                    print("Factorial of", num, "is", math.factorial(num))
                except:
                    print("Invalid input!")

            if math_choice == "2":
                try:
                    p = float(input("Enter Principal amount: "))
                    t = float(input("Enter Time (in years): "))
                    r = float(input("Enter Rate of interest (in %): "))
                    ci = p * ((1 + r / 100) ** t) - p
                    print("Solve Compound interest =", round(ci, 2))
                except:
                    print("Invalid input!")

            elif math_choice == "3":
                try:
                    angle = float(input("Enter angle in degrees: "))
                    rad = math.radians(angle)
                    print("sin(", angle, ") =", round(math.sin(rad), 4))
                    print("cos(", angle, ") =", round(math.cos(rad), 4))
                    print("tan(", angle, ") =", round(math.tan(rad), 4))
                except:
                    print("Invalid input!")

            elif math_choice == "4":
                print("Choose shape: 1. Circle 2. Rectangle")
                shape = input("Enter choice: ")
                if shape == "1":
                    r = float(input("Enter radius: "))
                    area = math.pi * r ** 2
                    print("Area of Circle:", round(area, 2))
                elif shape == "2":
                    l = float(input("Enter length: "))
                    w = float(input("Enter width: "))
                    print("Area of Rectangle:", l * w)
                else:
                    print("Invalid shape!")

            elif math_choice == "5":
                break

            else:
                print("Invalid choice!")

    elif main_choice == "3":
        while True:
            print("\n--- Random Data Generation ---")
            print("1. Generate Random Number")
            print("2. Generate Random List")
            print("3. Generate Random Password")
            print("4. Generate Random OTP")
            print("5.. Back to Main Menu")

            rand_choice = input("Enter your choice: ")

            if rand_choice == "1":
                print("Enter Random Number:", random.randint(1, 100))

            elif rand_choice == "2":
                print("Enter Random List:", random.choice("abcdefghijklmnopqrstuvwxyz"))

            elif rand_choice == "3":
                try:
                    length = int(input("Password length: "))
                    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
                    password = ''.join(random.choice(chars) for _ in range(length))
                    print("Generated password:", password)
                except:
                    print("Invalid input!")

            elif rand_choice == "4":
                try:
                    length = int(input("Enter OTP length: "))
                    ints = "1234567890"
                    OTP = ''.join(random.choice(ints) for _ in range(length))
                    print("Generated OTP:", OTP)
                except:
                    print("Invalid input!")

            elif rand_choice == "5":
                break

            else:
                print("Invalid choice!")

    elif main_choice == "4":
        print("\n--- UUID Generation ---")
        print("Generated UUID:", uuid.uuid4())

    elif main_choice == "5":
        while True:
            print("\n--- File Operations ---")
            print("1. Create a new file")
            print("2. Write to a file")
            print("3. Read from a file")
            print("4. Append to a file")
            print("5. Back to main menu")

            file_choice = input("Enter your choice: ")

            if file_choice == "1":
                fname = input("Enter file name: ")
                try:
                    open(fname, "w").close()
                    print("File created successfully!")
                except:
                    print("Error creating file!")

            elif file_choice == "2":
                fname = input("Enter file name: ")
                data = input("Enter data to write: ")
                try:
                    with open(fname, "w") as f:
                        f.write(data)
                    print("Data written successfully!")
                except:
                    print("Error writing to file!")

            elif file_choice == "3":
                fname = input("Enter file name: ")
                try:
                    with open(fname, "r") as f:
                        print("File Contents:\n", f.read())
                except:
                    print("File not found!")

            elif file_choice == "4":
                fname = input("Enter file name: ")
                data = input("Enter data to append: ")
                try:
                    with open(fname, "a") as f:
                        f.write("\n" + data)
                    print("Data appended successfully!")
                except:
                    print("Error appending to file!")

            elif file_choice == "5":
                break

            else:
                print("Invalid choice!")

    elif main_choice == "6":
        print("\n--- Explore Module Attributes ---")
        mod_name = input("Enter module name to explore: ")
        try:
            mod = __import__(mod_name)
            print("Available attributes in", mod_name, "module:")
            print(dir(mod))
        except:
            print("Module not found!")

    elif main_choice == "7":
        print("Thank you for using the Multi-Utility Toolkit!")
        break

    else:
        print("Invalid choice!")