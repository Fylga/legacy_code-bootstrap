import pytest
from src.storage import Storage

def test_new_account_has_initial_balance():
    """The initial balance is set to 1000.00 based on the cobol code."""
    account = Storage()
    assert account.get_balance() == 1000.00

def test_storage_with_custom_initial_balance():
    """Give the user the choice to set another initial balance."""
    account = Storage(6000)
    assert account.get_balance() == 6000.00

def test_write_balance_updates_balance():
    account = Storage()
    account.write_balance(5000)
    assert account.get_balance() == 5000.00