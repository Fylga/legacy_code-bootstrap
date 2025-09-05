import pytest
from decimal import Decimal
from src.datastore import DataStore

def test_new_account_has_initial_balance():
    account = DataStore()
    assert account.get_balance() == Decimal("1000.00")

def test_DataStore_with_custom_initial_balance():
    account = DataStore(Decimal("6000.00"))
    assert account.get_balance() == Decimal("6000.00")

def test_write_balance_updates_balance():
    account = DataStore()
    account.write_balance(Decimal("5000.00"))
    assert account.get_balance() == Decimal("5000.00")

def test_unvalid_initial_balance_raises_value_error():
    with pytest.raises(ValueError):
        DataStore(Decimal("-100"))
    with pytest.raises(ValueError):
        DataStore(Decimal("0"))
