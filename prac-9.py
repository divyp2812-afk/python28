import pandas as pd
import matplotlib.pyplot as plt 

df = None

print("====================== Data Analysis & Visualization Program ===========================")

while True:

    print("Please select an option")
    print("1. Load Dataset")
    print("2. Explore Data")
    print("3. Perform DataFram Operations")
    print("4. Handle Missing Data")
    print("5. Generate Descriptive statistics")
    print("6. Data Visualization")
    print("7. save Visualization")
    print("8. Exit")
    print("====================================================")

    choice = int(input("Enter your choice:"))

    if choice == 1:

        file = input("Enter CSV file name: ")
        try:
            df = pd.read_csv(file)
            print(" Data loaded successfully!")
        except Exception as e:
            print("Error loading file!")
            print("Error details:", e)

        print()

    elif choice == 2:

        print("== Explore Data == ")

        print("1. Display first 5 Rows")
        print("2. Display last 5 rows")
        print("3. Display column name")
        print("4. Display Data type")
        print("5. Display basic info")

        ex_choice = int(input("Enter your choice:"))

        if ex_choice == 1:
            print(df.head())
        elif ex_choice == 2:
            print(df.tail())
        elif ex_choice == 3:
            print(df.columns.to_list())
        elif ex_choice == 4:
            print(df.dtypes)
        elif ex_choice == 5:
            print(df.info())
        else:
            print("Invalid choice!")

    elif choice == 3:
        if df is None:
            print("Please load dataset first!")
        else:
            print("\n== Data Manipulation ==")
            print("1. Mathematical Operations on Column")
            print("2. Combine (Merge) Another CSV")
            print("3. Split Data by Column Value")

            op = input("Choose operation: ")

            if op == "1":
                col = input("Enter numeric column: ")
                if col in df.columns:
                    print("1. Add 10")
                    print("2. Subtract 10")
                    print("3. Multiply by 2")
                    print("4. Divide by 2")

                    ch = input("Choose: ")

                    if ch == "1":
                        df[col] = df[col] + 10
                    elif ch == "2":
                        df[col] = df[col] - 10
                    elif ch == "3":
                        df[col] = df[col] * 2
                    elif ch == "4":
                        df[col] = df[col] / 2
                    else:
                        print("Invalid option!")

                    print("Updated Data:")
                    print(df[[col]].head())
                else:
                    print("Column not found!")

            elif op == "2":
                try:
                    file2 = input("Enter second CSV file: ")
                    df2 = pd.read_csv(file2)

                    print("First file columns:", list(df.columns))
                    print("Second file columns:", list(df2.columns))

                    key = input("Enter common column to merge: ")

                    if key in df.columns and key in df2.columns:
                        df = pd.merge(df, df2, on=key)
                        print("Merged Successfully!")
                        print(df.head())
                    else:
                        print("Common column not found!")
                except:
                    print("Error merging files!")

            elif op == "3":
                col = input("Enter column to split by (Region/Product): ")
                if col in df.columns:
                    print("Available values:", df[col].unique())
                    val = input("Enter value: ")

                    new_df = df[df[col] == val]
                    print("Filtered Data:")
                    print(new_df.head())

                    save = input("Save to CSV? (y/n): ")
                    if save.lower() == "y":
                        name = input("Enter file name: ")
                        new_df.to_csv(name, index=False)
                        print("File saved!")
                else:
                    print("Column not found!")

            else:
                print("Invalid choice!")

    elif choice == 4:
        if df is None:
            print("Please load dataset first!")
        else:
            while True:
                print("\n1. Display rows with missin values")
                print("2. Fill missing values with mean")
                print("3. Drop rows with missing values")
                print("4. Replace missing values with a specific value")
                print("5. Back")

                sub = input("Enter choice: ")

                if sub == "1":
                    print(df[df.isnull().any(axis=1)])
                elif sub == "2":
                    df = df.apply(lambda c: c.fillna(c.mean()) if c.dtype != 'object' else c)
                    print("Filled with mean!")
                elif sub == "3":
                    df.dropna(inplace=True)
                    print("Rows dropped!")
                elif sub == "4":
                    v = input("Enter value: ")
                    df.fillna(v, inplace=True)
                    print("Replaced!")
                elif sub == "5":
                    break
                else:
                    print("Invalid choice!")

    elif choice == 5:
        if df is None:
            print("Please load dataset first!")
        else:
            print(df.describe())

    elif choice == 6:
        if df is None:
            print("Please load dataset first!")
        else:
            print("\n1. Bar Plot")
            print("2. Line Plot")
            print("3. Scatter Plot")
            print("4. Pie Chart")
            print("5. Histogram")
            print("6. Stack Plot")

            ch = input("Enter choice: ")
            plt.figure()

            if ch == "1":
                col = input("Column: ")
                if col in df.columns:
                    df[col].value_counts().plot(kind='bar')
            elif ch == "2":
                col = input("Column: ")
                if col in df.columns:
                    df[col].plot()
            elif ch == "3":
                x = input("X column: ")
                y = input("Y column: ")
                if x in df.columns and y in df.columns:
                    plt.scatter(df[x], df[y])
                    plt.xlabel(x); plt.ylabel(y)
            elif ch == "4":
                col = input("Column: ")
                if col in df.columns:
                    df[col].value_counts().plot(kind='pie', autopct='%1.1f%%')
                    plt.ylabel("")
            elif ch == "5":
                col = input("Column: ")
                if col in df.columns:
                    df[col].plot(kind='hist')
            elif ch == "6":
                print("Columns:", list(df.columns))
                cols = input("Enter columns comma separated: ").split(",")
                cols = [c.strip() for c in cols if c.strip() in df.columns]
                if len(cols) >= 2:
                    plt.stackplot(range(len(df)), *[df[c] for c in cols], labels=cols)
                    plt.legend()
            else:
                print("Invalid!")

            plt.show()
            last_plot = plt

    elif choice == 7:
        if last_plot is None:
            print("No graph to save!")
        else:
            name = input("Enter image name (graph.png): ")
            plt.savefig(name)
            print("Saved successfully!")

    elif choice == 8:
        print("Exiting the Program. Goodbye!")
        break

    else:
        print("Invalid Choice!")