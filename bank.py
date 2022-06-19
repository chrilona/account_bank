from __future__ import with_statement
from time import strftime


class Account:
    def __init__(self,account_name,account_number):
        self.account_name=account_name
        self.account_number=account_number
        self.balance=0
        self.deposit=[]
        self.withdraw=[]
        self.full_statement=[]
    def deposit(self,amount):
        self.balance+=amount
        if amount<=0:
            return f"Deposit must be positive"
        else:
            self.deposit.append(amount)
            return f"Your current balance is {self.balance}"
        
    def withdraw(self,amount):
        self.transaction=100
        if amount+self.transaction<self.balance:
            return f"You have insufficient funds"
        elif amount>self.balance:
            return f"Your balance is {self.balance}, you can't withdraw {amount}"
        else:
            self.withdraw.append(amount)
            self.balance -=amount +self.transaction
            return f"Hello {self.account_name} you have withdrawn {amount} your new balance is {self.balance} and your withdrawals are {self.withdrawals}"

    def deposit_statement(self):
        for amount in self.deposit:
            print(f"Your latest deposit is {amount}.Your total deposits are {sum(self.deposit)}")
    
    def withdrawal_statement(self):
        for withdraws in self.withdraw:
            print(f"Your most recent withdrawal is {withdraws}Ksh.You have withdrawn {len(self.withdraw)} times")

    def full_statement(self):
        for monies in self.full_statement:
            amount=monies["amount"]
            narration=monies["Narration"]
            time=monies["time"]
            date=strftime("%x/%X")
            print(f"{date} {narration} {amount}")

    def transfer(self,receiver,amount):
        self.receiver=receiver
        self.amount=amount
        current_balance=self.balance-amount
        if amount<=0:
            return f"You cannot transfer a non-existant amount"
        elif amount>self.balance:
            return f"Your cannot transfer {amount}.Your current balance is {self.balance}"
        elif amount<self.balance:
            return f"You have transfered {amount} to {self.receiver} your current balance is {current_balance}"

    def  borrow_loans(self,loan_amount):
        self.loan_amount=loan_amount
        self.interest=0.03*self.loan_amount
        self.total_loan=self.loan_amount+self.interest
        if len(self.deposits)>10 and loan_amount<=sum(self.deposits)//3 and loan_amount>100 and self.balance<0:
            print(f"You have been awarded a loan of {loan_amount} your current balance is {self.amount}")
        else:
            print("You are not eligible for a loan") 

    def pay_loans(self,amount_payloan):
        self.amount_payloan=amount_payloan
        self.interest=0.03*self.loan_amount
        total_topay=amount_payloan+self.interest
        loan_remaining=self.loan_amount-amount_payloan
        new_balance=self.loan_amount-total_topay
        if total_topay>0:
            print(f"You have deposited {amount_payloan} your loan of {self.loan_amount}Ksh.Your new loan balance is {new_balance}Ksh")
        elif total_topay>loan_remaining:
            print(f"Congratulations!! You have cleared your loan of {self.amount}.Your new balance is{new_balance}")
        else:
            print(f"You have a loan balance of {self.total_loan}")
    
    def current_balance(self):
        return self.balance
