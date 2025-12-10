print("Welcome to the Data Analyzer and Transformer Program:")
print()

print("Main Menu:-")
print()

while True:
    print("1. Input Data")
    print("2. Display Data Summary")
    print("3. Calculate Factorial")
    print("4. Filter Data by Threshold")
    print("5. Sort Data")
    print("6. Display Dataset Statistics")
    print("7. Exit Program")
    print()

    choice = int(input("Please enter your Choice:- "))

    if choice == 1:
        print()
        data = str(input("Enter data for 1D array  (separated by spaces):\n"))
        arr = list(map(int, data.split()))
        print(arr)
        print()
        print("Data has been stored successfully!")
        print()

    elif choice == 2:
        print()
        print("Data Summary:")
        print("- Total elements:", len(arr))
        print("- Minimum value:", min(arr))
        print("- Maximum value:", max(arr))
        print("- Sum of all value:", sum(arr))
        print("- Average value:", (sum(arr)//len(arr)))
        print()

    elif choice == 3:
        print()
        num = int(input("Enter a number to calculate its factorial:"))
        def factorial(n):
            """ this function work to find the factorial :-
            this function calcu;ate the factorial using recursion :- 
            
            using  this n*factorial (n-1)"""
            if n == 0 or n == 1:
                return 1
            else:
                return n * factorial(n-1)
        result = factorial(num)
        print()
        print(f"Factorial of {num} is: {result}")
        print(factorial._doc_)

    elif choice == 4:
        print()
        print("Enter a Threshold value to filter out data above this value:\n")

        threshold = int(input("Enter the threshold: "))

        
        filtered_data = list(filter(lambda x: x > threshold, arr))

        if len(filtered_data) <= 4:
            print("Filtered data:", filtered_data)
        else:
            print("Filtered data is:", filtered_data)

        print()

    elif choice == 5:
        print()
        print("Choose sorting option:")
        print("1. Ascending")
        print("2. Descending")
        print()

        Sort_choice = int(input("Enter your choice:"))
        print()

        if Sort_choice == 1:
            sorted_arr = sorted(arr)
            print("Sorted Data in Ascending Order:\n", sorted_arr)
            print()
        elif Sort_choice == 2:
            sorted_arr = sorted(arr, reverse=True)
            print("Sorted Data in Descending Order:\n", sorted_arr)
            print()
        else:
            print("Invalid order.")
            print()

    elif choice == 6:
        def maximum():
            m = arr[0]
            for choice in arr:
                if choice > m:
                    m = choice
            print("maximum value :-", m)

        maximum()

        def minimum():
            mi = arr[0]
            for choice in arr:
                if choice < mi:
                    mi = choice
            print("Minimum value :-", mi)

        minimum()

        def sum_values():
            global total
            total = 0
            for choice in arr:
                total = total + choice
            print("sum of all values :-", total)

        sum_values()

        def average():
            count = 0
            for choice in arr:
                count += 1
            avg = total / count
            print("average of values", avg)

        average()
        print(maximum._doc_)

    elif choice == 7:
        print("Thank you for using the Data Analyzer and Transformer Program. Goodbye!")
        break

    else:
        print("Invalid Choice, Try again!")