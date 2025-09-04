import pytest
from src.main import main

def _patch_inputs(monkeypatch, inputs):
  it = iter(inputs)
  monkeypatch.setattr('builtins.input', lambda prompt='': next(it))

def test_view_balance_and_exit(monkeypatch, capsys):
  """
  Integration: choose '1' to view balance, then '4' to exit.
  Verify menu printed, balance (initial 1000) appears, and program exits with message and return code 0.
  """
  _patch_inputs(monkeypatch, ["1", "4"])
  ret = main()
  captured = capsys.readouterr()
  assert ret == 0
  assert "Account Management System" in captured.out
  assert "Exiting the program. Goodbye!" in captured.out
  # initial balance expected from datastore is 1000.00; accept substring "1000"
  assert "1000" in captured.out

def test_invalid_choice_then_exit(monkeypatch, capsys):
  """
  Integration: choose an invalid option then exit.
  Expect an 'Invalid choice' message.
  """
  _patch_inputs(monkeypatch, ["9", "total", "4"])
  ret = main()
  captured = capsys.readouterr()
  assert ret == 0
  assert "Invalid choice" in captured.out
  assert "Invalid choice" in captured.out
  assert "Exiting the program. Goodbye!" in captured.out
