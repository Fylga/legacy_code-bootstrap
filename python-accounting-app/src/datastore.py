from decimal import Decimal, ROUND_HALF_UP
from abc import ABC, abstractmethod

class IDataStore:
    @abstractmethod
    def get_balance(self) -> Decimal:
        pass

    @abstractmethod
    def write_balance(self, amount: Decimal) -> None:
        pass

class DataStore(IDataStore):
    def __init__(self, balance: Decimal = Decimal("1000.00")):
        if balance <= 0:
            raise ValueError("Initial balance cannot be negative nor null.")
        self._balance = balance

    def get_balance(self) -> Decimal:
        return self._balance

    def write_balance(self, amount: Decimal) -> None:
        self._balance = amount
