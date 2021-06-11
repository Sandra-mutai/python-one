from datetime import datetime

class Account:
    def __init__ (self,name,phone):
        self.phone = phone
        self.name = name
        self.balance = 0
        self.loan = 0
        self.loanLimit = 1000

    def deposit(self,amount):
        try:
            1+amount
        except TypeError:
            return f"The amount must be in figures"
# If the amount input is in figures or not
        if amount<=0:
            return f"The amount must be greater than zero"
        else:
            self.balance+=amount
            return f"Dear {self.name} you have deposited {amount}. Your balance is {self.balance}"
    def show_balance(self):
        return self.balance
    def withdraw(self,amount):
        try:
            1+amount
        except TypeError:
            return f"The amount must be in figures"
        if amount <=0:
            return f"The amount must be greater than zero"
        elif amount>self.balance:
            return f"The amount withdrawn must be less than {self.balance}"
        else:
            self.balance-=amount
            transaction={"amount":amount,"balance":self.balance,"time":datetime.now(),"narration":"Withdraw"}
            return f"Your balance is {self.balance}"
    def borrow(self,amount):
        try:
            1+amount
        except TypeError:
            return f"The amount must be in figures"
        if amount<=self.loan_limit:
            self.loan+=amount
            self.balance+=self.loan
            transaction={"amount":amount,"balance":self.balance,"time":datetime.now(),"narration":"Loan"}
            return f"Dear {self.name}, you have borrowed KES{amount}.Your loan is KES{self.loan}, your balance is KES{self.balance}"
        else:
            return f"Your loan request of KES{amount} is unsuccessful because your loan limit is KES{self.loan_limit}"

    def get_statement(self):
            for transaction in self.transactions:
                narration=transaction["narration"]
                amount=transaction["amount"]
                balance=transaction["balance"]
                time=transaction["time"]
                print(f"{time.strftime('%D')}..{narration}..{amount}..{balance}..")
    def repay_loan(self,amount):
        try:
            1+amount
        except TypeError:
            return f"The amount must be in figures"
        if amount<0:
            return "Dear {self.name} amount has to be more than 0."
        elif amount<self.loan:
            self.loan-=amount
            return f"{amount} has been repaid towards your loan of KES {self.loan} your outstanding balance is KES{self.loan} "
        else:
            extra=amount-self.loan
            self.balance+=extra
            self.loan-=amount
            transaction={"amount":amount,"balance":self.balance,"time":datetime.now(),"narration":"Payments"}
            self.transactions.append(transaction)
            return f"Your loan has been fully paid.Your account balance is {self.balance}"

    def transfer(self,amount,account):
        try:
            1+amount
        except TypeError:
            return f"The amount must be in figures"

        if amount<0:
            return f" amount must be greater than 0"
        fee=amount*0.05

        if amount+fee>self.balance:
            return f"your balance is {self.balance}.You need {amount+fee} to be able to transfer"
        else:
            self.balance-=amount+fee
            account.deposit(amount)
            return f"Successful transfer! {self.name} has deposited KES{amount} to {account} account.Your balance is {self.balance}"

class MobileMoneyAccount(Account):
    def __init__(self,name,phone,service_provider):
        super().__init__(name,phone)
        self.service_provider=service_provider
        self.limit=300000
    def buy_airtime(self,amount):
        try:
            1+amount
        except TypeError:
            return f"The amount must be in figures"
        if amount<5:
            return f"Dear {self.name} you have to purchase KES 5 or more"
        else:
            self.balance-=amount
            return f"Dear {self.name} you have successfully purchased {amount} airtime.Your new balance is{self.balance}successful because your loan limit is KES{self.loan_limit}"