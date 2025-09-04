from datastore import DataStore

class Operations:
    def __init__(self, storage: DataStore):
        self.storage = storage

    def total(self) -> None:
        print(f"Current balance: {self.storage.get_balance():.2f}")

