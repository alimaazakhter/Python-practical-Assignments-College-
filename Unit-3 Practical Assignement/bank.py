from abc import ABC, abstractmethod

# 1. Interface

class AccountInterface(ABC):

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def check_balance(self):
        pass


# 2. BankAccount Base Class

class BankAccount(AccountInterface):

    total_accounts = 0   # Static Variable

    def __init__(self, holder, mobile, acc_type, balance):
        self.account_holder = holder
        self.mobile_number = mobile
        self.account_type = acc_type
        self.__balance = balance     # Private Variable (Encapsulation)

        BankAccount.total_accounts += 1
        self.account_number = BankAccount.total_accounts

    def deposit(self, amount):
        self.__balance += amount
        print("Amount Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Amount Withdrawn:", amount)
        else:
            print("Insufficient Balance!")

    def check_balance(self):
        print("Current Balance:", self.__balance)

    @staticmethod
    def get_total_accounts():
        return BankAccount.total_accounts

    @classmethod
    def update_total_accounts(cls, value):
        cls.total_accounts = value


# 3. SavingsAccount Class
class SavingsAccount(BankAccount):

    def __init__(self, holder, mobile, balance, interest_rate):
        super().__init__(holder, mobile, "Savings", balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self._BankAccount__balance * self.interest_rate / 100
        self.deposit(interest)
        print("Interest Applied!")


# 4. CheckingAccount Class
class CheckingAccount(BankAccount):

    def __init__(self, holder, mobile, balance, overdraft_limit):
        super().__init__(holder, mobile, "Checking", balance)
        self.overdraft_limit = overdraft_limit

    # Polymorphism (Method Overriding)
    def withdraw(self, amount):
        if amount <= self._BankAccount__balance + self.overdraft_limit:
            self._BankAccount__balance -= amount
            print("Amount Withdrawn with Overdraft:", amount)
        else:
            print("Overdraft Limit Exceeded!")


# 5. LoanAccount (Abstract Class)

class LoanAccount(ABC):

    @abstractmethod
    def apply_loan(self, amount):
        pass

    @abstractmethod
    def repay_loan(self, amount):
        pass


# 6. PersonalLoanAccount Class
class PersonalLoanAccount(LoanAccount):

    def __init__(self):
        self.loan_balance = 0

    def apply_loan(self, amount):
        self.loan_balance += amount
        print("Loan Applied:", amount)

    def repay_loan(self, amount):
        self.loan_balance -= amount
        print("Loan Repaid:", amount)


# MAIN PROGRAM

print("\n--- SAVINGS ACCOUNT ---")
s1 = SavingsAccount("Ali", "9876543210", 5000, 5)
s1.deposit(1000)
s1.withdraw(2000)
s1.apply_interest()
s1.check_balance()

print("\n--- CHECKING ACCOUNT ---")
c1 = CheckingAccount("Rohan", "9998887776", 3000, 1500)
c1.deposit(500)
c1.withdraw(4000)
c1.check_balance()

print("\n--- PERSONAL LOAN ACCOUNT ---")
l1 = PersonalLoanAccount()
l1.apply_loan(10000)
l1.repay_loan(3000)
print("Loan Balance:", l1.loan_balance)

print("\nTotal Accounts Created:", BankAccount.get_total_accounts())
