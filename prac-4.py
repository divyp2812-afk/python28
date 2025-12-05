print("Welcome to the Data Analyzer and Transformer Program")
print()

print("Main Menu:")
print()

while True:
    print("\n1. Input Data")
    print("2. Display Data Summary")
    print("3. Calculate Factorial")
    print("4. Filter Data by Threshold")
    print("5. Sort Data")
    print("6. Display Dataset Statistics")
    print("7. Exit Program")
    print()

    choice = int(input("Please enter your Choice: "))

    if choice == 1:
        data = str(input("Enter data for 1D array(separated by spaces): "))
        arr = list(map(int,data.split()))
        print(arr)
        print()
        print("Data has been stored successfully!")

    elif choice == 2:
        print("\nData Summary:")
        print("-Total elements:", len(arr))
        print("-Minimum value:", min(arr))
        print("-Maximum value:", max(arr))
        print("-Sum of all value:", sum(arr))
        print("-Average value:", (sum(arr)//len(arr)))

    elif choice == 3:
        num = int(input("Enter a number to calculate its factorial:"))
        def factorial(n):
            if n == 0 or n == 1:
                return 1
            else:
                return n * factorial(n-1)
        result = factorial(num)
        print(f"Factorial of {num} is: {result}")

    elif choice == 4:
        num = int(input("Enter a Threshold value to filter out data above this value:"))
        
        def filtered_data(data, threshold):
            return [x for x in data if threshold <= x]
        if len == 0:
            print("Null")
        else:
            result = filtered_data(arr,num)
            print("Filtered Data:",result)
            
    elif choice == 5:
        print("\nChoose sorting option:")
        print("1. Ascending")
        print("2. Descending")

        Sort_choice = int(input("Enter your choice:"))

        if Sort_choice == 1:
            sorted_arr = sorted(arr)
            print("Sorted Data in Ascending Order:",sorted_arr)
        elif Sort_choice == 2:
            sorted_arr = sorted(arr, reverse=True)
            print("Sorted Data in Descending Order:",sorted_arr)
        else:
            print("Invalid Option.")

    elif choice == 6:
        print("\nDataset Statistics:")
        print("-Minimum value:", min(arr))
        print("-Maximum value:", max(arr))
        print("-Sum of all value:", sum(arr))
        print("-Average value:", sum(arr)//len(arr))

    elif choice == 7:
        print("Thank you for using the Data Analyzer and Transformer Program. Goodbye!")
    
    else:
        print("Invalid Choice, Try again!")
    

    



            



        
        
   





