from datastore import IDataStore
from decimal import Decimal

class Operations:
    def __init__(self, storage: IDataStore):
        self.storage = storage

    def total(self) -> None:
        print(f"Current balance: {self.storage.get_balance():.2f}")

    def credit(self) -> None:
        try:
          amount = Decimal(input("Enter credit amount: "))
        except:
          print("Invalid amount. Please enter a numeric value.")
          return

        if amount < 0:
          print("Credit amount must be positive.")
          return

        current_balance = self.storage.get_balance()
        self.storage.write_balance(current_balance + amount)
        print(f"Amount credited. New balance: {self.storage.get_balance():.2f}")
    
    def debit(self) -> None:
        try:
          amount = Decimal(input("Enter debit amount: "))
        except:
          print("Invalid amount. Please enter a numeric value.")
          return

        if amount < 0:
          print("Debit amount must be positive.")
          return

        current_balance = self.storage.get_balance()
        if amount > current_balance:
          print("Insufficient funds for this debit.")
          return

        self.storage.write_balance(current_balance - amount)
        print(f"Amount debited. New balance: {self.storage.get_balance():.2f}")

        