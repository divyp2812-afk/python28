import numpy as np

print("Welcome to the NumPy Analyzer!")
print("=======================================")

while True:
    print("\nChoose an option:")
    print("1. Create a numpy Array")
    print("2. Perfrom mathematical Operations")
    print("3. Combine or Split Arrays")
    print("4. Search , Sort, or Filter Arrays")
    print("5. Compute Aggregates and Statistics")
    print("6. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\nSelect the type of array to create:")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")

        array_choice = int(input("Enter your choice: "))

        
        if array_choice == 1:
            elements = list(map(int, input("Enter elements separated by space: ").split()))
            arr = np.array(elements)
            print("Array created:", arr)

       
        elif array_choice == 2:
            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of columns: "))
            elements = list(map(int, input(f"Enter {rows*cols} elements: ").split()))
            arr1 = np.array(elements).reshape(rows, cols)
            print("Array created:\n", arr1)

       
        elif array_choice == 3:
            depth = int(input("Enter depth: "))
            rows = int(input("Enter rows: "))
            cols = int(input("Enter columns: "))
            elements = list(map(int, input(f"Enter {depth*rows*cols} elements: ").split()))
            arr = np.array(elements).reshape(depth, rows, cols)
            print("Array created:\n", arr)

        else:
            print("Invalid array type!")
            continue

        print("\nChoose an operation:")
        print("1. Indexing")
        print("2. Slicing")
        print("3. Go Back")

        operation = int(input("Enter your choice: "))

        if operation == 1:
            r = int(input("Enter row index: "))
            c = int(input("Enter column index: "))
            print("Element:", arr[r][c])

        elif operation == 2:
            r_range = input("Enter row range (start:end): ")
            c_range = input("Enter column range (start:end): ")

            arr = np.array(elements).reshape(rows, cols)

            r_s, r_e = map(int, r_range.split(":"))
            c_s, c_e = map(int, c_range.split(":")) 

            sliced = arr[r_s:r_e, c_s:c_e]
            print("Sliced Array:\n", sliced)

        elif operation == 3:
            continue

        else:
            print("Invalid operation!")


    elif choice == 2:

        print("\nChoose a mathematical operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
    
        math_choice = int(input("Enter your choice: "))

        if math_choice in [1, 2, 3, 4]:
            size = int(input("Enter the size of the arrays: "))

            print("Original array:\n",arr1)

            print("Enter elements for the second array:")
            element2 = list(map(int, input(f"Enter {rows*cols} elements for second array: ").split()))
            arr2 = np.array(element2).reshape(rows, cols)

            print(arr2)
            if math_choice == 1:
                print("Result:\n", arr1 + arr2)
            elif math_choice == 2:
                print("Result:\n", arr1 - arr2)
            elif math_choice == 3:
                print("Result:\n", arr1 * arr2)
            elif math_choice == 4:
                if 0 in arr2:
                    print("Error: Division by zero!")
                else:
                    print("Result:\n", arr1 / arr2)
            else:
                print("Invalid operation!")

        else:
            print("Invalid mathematical operation choice!")

    elif choice == 3:

        print("\nChoose an option:")
        print("1. Combine Arrays")
        print("2. Split Array")

        arr_choice = int(input("Enter your choice:"))

        if arr_choice == 1:

            print("Original array:\n",arr1)

            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of columns: "))
            elements = list(map(int, input(f"Enter {rows*cols} elements: ").split()))
            arr2 = np.array(elements).reshape(rows, cols)
            print("Second Array:\n", arr2)

            print("Combined Array(Vertical Stack):\n", np.vstack((arr1, arr2))) 

        elif arr_choice == 2:
                
            print("Original array:\n", arr1)
            num_splits = int(input("Enter number of splits: "))
            split_arr = np.vsplit(arr1, num_splits)
            print("Split Arrays (Vertically):", split_arr)

        else:
            print("Invalid choice!")
    
    elif choice == 4:

        print("\nChoose an options:")
        print("1. Search a value")
        print("2. Sort the array")
        print("3. Filter values")

        sub = int(input("Enter your choice:"))

        if sub == 1:
            print("Original array:\n",arr1)

            value = int(input("Enter the value to search:"))
            result = np.where(arr1 == value)
            print(result)

        elif sub == 2:
            print("Original array:\n",arr1)

            sorted_arr = np.sort(arr1)
            print("Sorted Array:\n", sorted_arr)

        elif sub == 3:
           x = int(input("Show values greater than: "))
           print("Filtered values:", arr1[arr1 > x]) 

        else:
            print("Invalid choice!")
    
    elif choice == 5:

        print("\nChoose an aggregate/statistical operation:")
        print("1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")

        agg_choice = int(input("Enter your choice:"))

        print("Original array:\n",arr1)

        if agg_choice == 1:
            print("Sum:", np.sum(arr1)) 
        elif agg_choice == 2:     
            print("Mean:", np.mean(arr1))   
        elif agg_choice == 3:
            print("Median:", np.median(arr1))
        elif agg_choice == 4: 
            print("Standard Deviation:", np.std(arr1))
        elif agg_choice == 5: 
            print("Variance:", np.var(arr1))
        else:
            print("Invalid aggregate choice!")

    elif choice == 6:
        print("Thank you for using NumPy Analyzer!")
        break

    else:
        print("Invalid Menu Choice.")