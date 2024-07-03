class Account:
    def __init__(self, number_agency, balance=0):
        self._balance = balance
        self.number_agency = number_agency
        
    def deposit(self, valor):
        self._balance += valor
    
    def withdraw(self, valor):
        self._balance -= valor
    
account = Account("0011", 100)
account.deposit(100)

print(account._balance) # atributo privado
print(account.number_agency) # atributo público
