from datetime import datetime, time
now=datetime.now()
class Account:
    def __init__(self,name,phone,account,loan_limit) :
        self.name=name
        self.phone=phone
        self.account=account
        self.balance=0
        self.loan=0
        self.loan_limit=loan_limit
        self.transaction=[]
        self.repay_loan=[]
        self.borrow=[]
        self.withdraw=[]


    # def show(self,balance):
    #     return self.balance

    def deposit(self,amount):
        if amount <=0:
            return f"the amount must be grater than zero"
        else:
            self.balance +=amount
            transaction={
                "amount":amount,
                "balance":self.balance,
                "time":now.strftime ("%D"),
                "narration":"Deposit"
                }
            self.transaction.append(transaction)
            return f"dear {self.name} you have deposited KES {amount} your new balance is {self.balance}"

    def withdraw(self,amount):
        if amount <=0:
            return "the amount must be grater than zero"
        elif (amount<self.balance):
            return "the amount must be less than the balance"
        else:
            self.balance+=amount
            withdraw={
                "amount":amount,
                "balance":self.balance,
                "time":now.strftime ("%D"),
                "narration":"Deposit"
                }
            self.withdraw.append(withdraw)
            return f"dear {self.name} you have deposited KES {amount} your new balance is {self.balance}"
    def borrow(self,amount):
        if amount<=self.loan_limit:
            return f"you are above your loan limit"
        elif self.loan>0:
            return f"you cant borrow loan"
        else:
            self.loan+=1
            self.balance+=amount
            borrow={
                "amount":amount,
                "balance":self.balance,
                "time":now.strftime ("%D"),
                "narration":"Deposit"
                }
            self.borrow.append(borrow)
            return f"dear {self.name} you have deposited KES {amount} your new balance is {self.balance}"    
    def get_statement(self):
        for transaction in self.transaction:
            narration =transaction["narration"]
            amount =transaction["amount"]
            balance =transaction["balance"]
            time =transaction["time"]
            print(f"{time}{narration}{amount} balance {balance}")

    def repay_loan(self,amount):
        if amount<=0:
            return f"you are above your loan limit"
        elif amount<self.loan:
            self.loan-=amount
            return f"amount has been reduced"
        else:
            extra=amount-self.loan
            self.balance+=extra
            repay_loan={
                "amount":amount,
                "balance":self.balance,
                "time":now.strftime ("%D"),
                "narration":"Deposit"
                }
            self.transaction(repay_loan)
            return f"dear {self.name} you have repay your loan and your balance is {self.balance}"

