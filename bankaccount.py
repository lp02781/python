def BankAccount():
    def __init__(self, balance=0):
        self.balance=balance
    def withdraw(self, amount):
        self.balance-=amount
    def deposit(self, amount):
        self.balance+=amount
    def balance(self):
        return self.balance

duit=BankAccount()
duit.deposit()
print(duit.balance())
duit.withdraw(200000)
print(duit.balance())

        
