import pytest
from decimal import Decimal
from src.operations import Operations
from src.datastore import IDataStore

# --- Mock DataStore ---
class MockDataStore(IDataStore):
    """Mock datastore for testing Operations independently of DataStore."""
    def __init__(self, balance=Decimal("1000.00")):
        self._balance = balance

    def get_balance(self) -> Decimal:
        return self._balance

    def write_balance(self, amount: Decimal) -> None:
        self._balance = amount

# --- Helper to patch input ---
def _patch_inputs(monkeypatch, inputs):
    it = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda prompt='': next(it))

# --- Fixtures ---
@pytest.fixture
def mock_storage():
    return MockDataStore()

@pytest.fixture
def operations(mock_storage):
    return Operations(mock_storage)

# --- Tests ---

def test_total_prints_balance(operations, capsys):
    operations.total()
    captured = capsys.readouterr()
    assert "Current balance: 1000.00" in captured.out

def test_credit_valid_amount(monkeypatch, operations, capsys):
    _patch_inputs(monkeypatch, ["50.25"])
    operations.credit()
    captured = capsys.readouterr()
    assert "Amount credited. New balance: 1050.25" in captured.out

def test_credit_invalid_amount(monkeypatch, operations, capsys):
    _patch_inputs(monkeypatch, ["money"])
    operations.credit()
    captured = capsys.readouterr()
    assert "Invalid amount. Please enter a numeric value." in captured.out

def test_credit_negative_amount(monkeypatch, operations, capsys):
    _patch_inputs(monkeypatch, ["-20"])
    operations.credit()
    captured = capsys.readouterr()
    assert "Credit amount must be positive." in captured.out

def test_credit_scientific_notation(monkeypatch, operations, capsys):
    _patch_inputs(monkeypatch, ["1e2"])
    operations.credit()
    captured = capsys.readouterr()
    # 1000 + 100 = 1100
    assert "Amount credited. New balance: 1100.00" in captured.out

def test_credit_comma_input(monkeypatch, operations, capsys):
    _patch_inputs(monkeypatch, ["20,00"])
    operations.credit()
    captured = capsys.readouterr()
    assert "Invalid amount. Please enter a numeric value." in captured.out

def test_debit_valid_amount(monkeypatch, operations, capsys):
    _patch_inputs(monkeypatch, ["200.50"])
    operations.debit()
    captured = capsys.readouterr()
    # 1000 - 200.50 = 799.50
    assert "Amount debited. New balance: 799.50" in captured.out

def test_debit_invalid_amount(monkeypatch, operations, capsys):
    _patch_inputs(monkeypatch, ["abc"])
    operations.debit()
    captured = capsys.readouterr()
    assert "Invalid amount. Please enter a numeric value." in captured.out

def test_debit_negative_amount(monkeypatch, operations, capsys):
    _patch_inputs(monkeypatch, ["-10"])
    operations.debit()
    captured = capsys.readouterr()
    assert "Debit amount must be positive." in captured.out

def test_debit_insufficient_funds(monkeypatch, operations, capsys):
    _patch_inputs(monkeypatch, ["2000"])
    operations.debit()
    captured = capsys.readouterr()
    assert "Insufficient funds for this debit." in captured.out

def test_debit_scientific_notation(monkeypatch, operations, capsys):
    _patch_inputs(monkeypatch, ["1e2"])
    operations.debit()
    captured = capsys.readouterr()
    # 1000 - 100 = 900
    assert "Amount debited. New balance: 900.00" in captured.out

def test_debit_comma_input(monkeypatch, operations, capsys):
    _patch_inputs(monkeypatch, ["20,00"])
    operations.debit()
    captured = capsys.readouterr()
    assert "Invalid amount. Please enter a numeric value." in captured.out

def test_credit_and_debit_flow(monkeypatch, operations, capsys):
    """Combined flow: credit + debit"""
    _patch_inputs(monkeypatch, [
        "150.75",  # credit
        "50.25"    # debit
    ])
    operations.credit()
    operations.debit()
    captured = capsys.readouterr()
    # 1000 + 150.75 - 50.25 = 1100.50
    assert "Amount credited. New balance: 1150.75" in captured.out
    assert "Amount debited. New balance: 1100.50" in captured.out
