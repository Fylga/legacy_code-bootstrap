import pytest
from src.operations import Operations
from src.datastore import DataStore
from src.main import main

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

def _patch_inputs(monkeypatch, inputs):
  it = iter(inputs)
  monkeypatch.setattr('builtins.input', lambda prompt='': next(it))

def test_credit_valid_amount(monkeypatch, capsys):
  _patch_inputs(monkeypatch, ["2", "19.99", "4"])
  ret = main()
  captured = capsys.readouterr()
  assert "1019.99" in captured.out

def test_credit_value_with_comma(monkeypatch, capsys):
  _patch_inputs(monkeypatch, ["2", "20,00", "4"])
  ret = main()
  captured = capsys.readouterr()
  assert "Invalid amount. Please enter a numeric value." in captured.out

def test_credit_value_with_scientific_notation(monkeypatch, capsys):
  _patch_inputs(monkeypatch, ["2", "1e2", "4"])
  ret = main()
  captured = capsys.readouterr()
  assert "1119.99" in captured.out

def test_credit_unvalid_amount(monkeypatch, capsys):
  _patch_inputs(monkeypatch, ["2", "-20", "4"])
  ret = main()
  captured = capsys.readouterr()
  assert "Credit amount must be positive." in captured.out

def test_credit_unvalid_value(monkeypatch, capsys):
  _patch_inputs(monkeypatch, ["2", "money", "4"])
  ret = main()
  captured = capsys.readouterr()
  assert "Invalid amount. Please enter a numeric value." in captured.out

def test_debit_valid_amount(monkeypatch, capsys):
  _patch_inputs(monkeypatch, ["3", "19.99", "4"])
  ret = main()
  captured = capsys.readouterr()
  assert "1100.00" in captured.out

def test_debit_value_with_comma(monkeypatch, capsys):
  _patch_inputs(monkeypatch, ["3", "20,00", "4"])
  ret = main()
  captured = capsys.readouterr()
  assert "Invalid amount. Please enter a numeric value." in captured.out

def test_debit_value_with_scientific_notation(monkeypatch, capsys):
  _patch_inputs(monkeypatch, ["3", "1e2", "4"])
  ret = main()
  captured = capsys.readouterr()
  assert "1000.00" in captured.out

def test_debit_unvalid_amount(monkeypatch, capsys):
  _patch_inputs(monkeypatch, ["3", "-20", "4"])
  ret = main()
  captured = capsys.readouterr()
  assert "Debit amount must be positive." in captured.out

def test_debit_unvalid_value(monkeypatch, capsys):
  _patch_inputs(monkeypatch, ["3", "money", "4"])
  ret = main()
  captured = capsys.readouterr()
  assert "Invalid amount. Please enter a numeric value." in captured.out

def test_debit_unsufficient_fund(monkeypatch, capsys):
  _patch_inputs(monkeypatch, ["3", "20000", "4"])
  ret = main()
  captured = capsys.readouterr()
  assert "Insufficient funds for this debit." in captured.out