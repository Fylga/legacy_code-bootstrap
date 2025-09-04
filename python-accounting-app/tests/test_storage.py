import pytest
from src.datastore import DataStore

def test_new_account_has_initial_balance():
    """The initial balance is set to 1000.00 based on the cobol code."""
    account = DataStore()
    assert account.get_balance() == 1000.00

def test_DataStore_with_custom_initial_balance():
    """Give the user the choice to set another initial balance."""
    account = DataStore(6000)
    assert account.get_balance() == 6000.00

def test_write_balance_updates_balance():
    account = DataStore()
    account.write_balance(5000)
    assert account.get_balance() == 5000.00

def test_unvalid_initial_balance_raises_value_error():
    with pytest.raises(ValueError):
        DataStore(-100)  # Negative initial balance should raise ValueError
    with pytest.raises(ValueError):
        DataStore(0)     # Zero initial balance should raise ValueError
