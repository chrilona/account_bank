from __future__ import with_statement


class Account:
    def __init__(self,account_name,account_number):
        self.account_name=account_name
        self.account_number=account_number
        self.balance=0
        self.deposit=[]
        self.withdraw=[]
    def deposit(self,amount):
        self.balance+=amount
        if amount<=0:
            return f"Deposit must be positive"
        else:
            self.deposit.append(amount)
            return f"Your current balance is {self.balance}"
        
    def withdraw(self,amount):
        self.transaction=100
        if amount<=0:
            return f"Withdraw must be greater than zero"
        elif amount>self.balance:
            return f"Your balance is {self.balance}, you can't withdraw {amount}"
        else:
            self.withdraw.append(amount)
            self.balance -=amount +self.transaction
            return f"Hello {self.account_name} you have withdrawn {amount} your new balance is {self.balance} and your withdrawals are {self.withdrawals}"
    def deposit_statement(self):
        for amount in self.deposit:
            print(amount, end="\n")
    
    def with_statement(self):
        for v in self.deposit:
            print(v,end="\n")
    
    def current_balance(self):
        return self.balance
