import pytest
from src.operations import Operations
from src.datastore import DataStore

@pytest.fixture
def datastore():
    return DataStore()

@pytest.fixture
def operations(datastore):
    return Operations(datastore)

def test_total_prints_balance(operations, capsys):
    operations.total()
    captured = capsys.readouterr()
    assert "Current balance: 1000.00" in captured.out


