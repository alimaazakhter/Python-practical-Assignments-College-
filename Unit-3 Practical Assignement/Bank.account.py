class Account:

    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no

    def debit(self, amount):
        self.balance -= amount
        print("Rs. ", amount, "was Debited ")
        print("Your total balance: ", self.total_amt())

    def credit(self, amount):
        self.balance += amount 
        print("Rs. ", amount, "was Credited")
        print("Your total balance: ", self.total_amt())

    def total_amt(self):
        return self.balance         

acc1 = Account(10000, "ACC1@1234") 
acc1.debit(500)   
acc1.credit(1000)
