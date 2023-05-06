class Bank:
    balance = 0

    def __init__(self, name,number,branch):
        self.account_name = name
        self.account_number = number
        self.account_branch = branch

    def deposit(self, amt):
        self.balance+=amt
        return f"You have withdrawn {amt}. Your new balance is {self.balance} ksh"
    
    def withdraw(self, amt):
        self.balance-=amt
        return f"You have withdrawn ksh{amt}. Your new balance is {self.balance}"
    
    def status(self):
        if self.balance==0:
            return f"Your account is dormant"
        else:
            return f"Your account is active"
        
account1 = Bank("Equity", 10234747823, "Moi Avenue")
account2 = Bank("NCBA", 11388586995, "Ngong Road")

print(account1.deposit(20000))
print(account1.withdraw(1000))
print(account1.status())

print(account2.deposit(2000000))
print(account2.withdraw(100000))
print(account2.status())

