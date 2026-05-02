import pytest

class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Invalid deposit amount")
        self.balance += amount

def test_deposit_success():
    account = BankAccount()
    account.deposit(100)
    assert account.balance == 100

def test_deposit_multiple(): 
    account = BankAccount()
    account.deposit(100)
    account.deposit(50)
    assert account.balance == 150

def test_deposit_invalid_amount():
    account = BankAccount()
    with pytest.raises(ValueError):
        account.deposit(-50)