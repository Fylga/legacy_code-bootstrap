from decimal import Decimal, ROUND_HALF_UP

class Storage:
    def __init__(self, balance: Decimal = Decimal("1000.00")):
        self._balance = balance

    def get_balance(self) -> Decimal:
        return self._balance

    def write_balance(self, amount: Decimal) -> None:
        self._balance = amount
