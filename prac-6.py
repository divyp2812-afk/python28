print("Welcome to Personal Journal Manager!")
print("Select an option from the menu below.")

from datetime import datetime

class JournalManager:
    def __init__(self, filename="journal.txt"):
        self.filename = filename

    def add_entry(self):
        try:
            entry = input("Type your journal entry:\n")
            time = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

            with open(self.filename, "a") as file:
                file.write(f"{time}\n{entry}\n{'='*40}\n")  

            print("\nEntry saved successfully!")
        except Exception as e:
            print("Error while saving entry:", e)

    def view_entry(self):
        try:
            with open(self.filename, "r") as file:
                print("\n--- All Journal Entries ---")
                print(file.read())
        except FileNotFoundError:
            print("\nNo entries found. Please add one first!")
        except Exception as e:
            print("Error occurred:", e)

    def search_entry(self):
        try:
            keyword = input("Enter keyword or date (YYYY-MM-DD) to search: ")

            with open(self.filename, "r") as file:
                found = False
                for line in file:
                    if keyword.lower() in line.lower():
                        print("Found:", line.strip())  
                        found = True

            if not found:
                print("No entries found for your search.")
        except FileNotFoundError:
            print("Journal file not found.")
        except Exception as e:
            print("Error occurred:", e)

    def delete_entries(self):
        try:
            confirm = input("Confirm delete ALL entries? (yes/no): ")
            if confirm.lower() == "yes":
                with open(self.filename, "w") as file:
                    pass
                print("All entries deleted.")
            else:
                print("Delete cancelled.")
        except Exception as e:
            print("Error occurred:", e)


Journal = JournalManager()

while True:
    print("\n--- Journal Menu ---")
    print("1. Add Entry")
    print("2. View Entries")
    print("3. Search Entries")
    print("4. Delete Entries")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice (1-5): "))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 5.")
        continue

    if choice == 1:
        Journal.add_entry()
    elif choice == 2:
        Journal.view_entry()
    elif choice == 3:
        Journal.search_entry()
    elif choice == 4:
        Journal.delete_entries()
    elif choice == 5:
        print("Goodbye! Exiting Personal Journal Manager.")
        break
    else:
        print("Invalid choice. Please try again.")