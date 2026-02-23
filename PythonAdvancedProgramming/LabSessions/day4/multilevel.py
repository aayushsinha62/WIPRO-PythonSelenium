# Level 1 (Grandparent)
class Account:
    def __init__(self, balance):
        self.balance = balance


# Level 2 (Parent)
class SavingsAccount(Account):
    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)
        print("Balance after deposit:", self.balance)


# Level 3 (Child)
class InterestAccount(SavingsAccount):
    def addInterest(self, rate):
        interest = self.balance * rate / 100
        self.balance += interest
        print("Interest added:", interest)
        print("Final balance:", self.balance)


# Object creation
acc = InterestAccount(1000)

acc.deposit(500)       # from SavingsAccount
acc.addInterest(5)     # from InterestAccount