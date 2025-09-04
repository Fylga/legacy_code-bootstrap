from operations import Operations
from datastore import DataStore

storage = DataStore()
operations = Operations(storage)
actions = {
    "1": operations.total,
    "2": operations.credit,
    "3": operations.debit,
}

def main():
  while True:
    print("\n--------------------------------")
    print("Account Management System")
    print("1. View Balance")
    print("2. Credit Account")
    print("3. Debit Account")
    print("4. Exit")
    print("--------------------------------")

    choice = input("Enter your choice (1-4): \n")
    if choice == "4":
      print("Exiting the program. Goodbye!")
      break
    action = actions.get(choice)
    if action:
      action()
    else:
      print("Invalid choice, please select 1-4.")

  return 0

if __name__ == "__main__": # pragma: no cover
    main()