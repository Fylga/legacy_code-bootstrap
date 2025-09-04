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