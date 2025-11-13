print("Welcome to the pattern Generator and Number Analyzer!")

while True:
    print("1. Generate a Pattern")
    print("2. Analyze a range of number")
    print("3. Exit")

    choice=int(input("choose number:"))

    if choice == 1:
        rows=int(input("Enter rows"))

        for i in range (1,rows+1):
            print("*"*i)
        
    elif choice == 2:
        num1=int(input("Enter starting number:"))
        num2=int(input("Enter ending number:"))
        total=0

        for n in range(num1,num2+1):
            if n % 2 == 0:
                print("Number is even",n)
            else:
                print("Number is odd",n)

            total += n

            print(f"Total is from {num1} to {num2} are",total)

    elif choice == 3:
        print("NULL")

        exit()
    
    else:
        print("Invalid choice",choice)




