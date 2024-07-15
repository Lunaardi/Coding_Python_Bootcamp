import textwrap
from abc import ABC
from datetime import datetime

class ContasIterador:
    def __init__(self, accounts):
        self.accounts = accounts
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            account = self.accounts[self._index]
            return f"""\
            Agência:\t{account.agency}
            Número:\t\t{account.account_number}
            Titular:\t{account.customer.nome}
            Saldo:\t\tR$ {account.balance:.2f}
        """
        except IndexError:
            raise StopIteration
        finally:
            self._index += 1


class Customer:
    def __init__(self, address):
        self.address = address
        self.accounts = []

    def carry_out_transaction(self, account, transaction):
        if len(account.historic.transaction_day()) >= 10:
            print("You have exceeded the number of transactions allowed for today!!")
            return
        
        transaction.register(account)

    def add_account(self, account):
        self.accounts.append(account)

class PhysicalPerson(Customer):
    def __init__(self, name, birth_date, cpf, address):
        super().__init__(address)
        self.name = name
        self.birth_date = birth_date
        self.cpf = cpf

class Account:
    def __init__(self, account_number, customer):
        self._balance = 0
        self._account_number = account_number
        self._agency = "0011"
        self._customer = customer
        self._historic = Historic()
			

    @classmethod
    def new_account(cls, customer, account_number):
        return cls(account_number, customer)

    @property
    def balance(self):
        return self._balance

    @property
    def account_number(self):
        return self._account_number

    @property
    def agency(self):
        return self._agency

    @property
    def customer(self):
        return self._customer

    @property
    def historic(self):
        return self._historic

    def to_withdraw(self, value):
        balance = self.balance
        exceeded_balance = value > balance

        if exceeded_balance:
            print("Operation Failed! You don't have enough balance.")

        elif value > 0:
            self._balance -= value
            print(f"withdrawal in the amount of R$: {value:.2f} made successfully!")
            return True

        else:
            print("Operation Failed! The value entered is invalid.")

        return False

    def deposit(self, value):
        if value > 0:
            self._balance += value
            print(f"Deposit made successfully!")
            
        else:
            print("Operation Failed! The value entered is invalid.")
            return False

        return True

class CurrentAccount(Account):
    def __init__(self, account_number, customer, limit=500, limit_withdraw=3):
        super().__init__(account_number, customer)
        self._limit = limit
        self._limit_withdraw = limit_withdraw

    def to_withdraw(self, value):
        number_withdraw = len(
            [transaction for transaction in self.historic.transactions if transaction["type"] == Withdral.__name__]
        )

        exceeded_limit = value > self._limit
        exceeded_withdraw = number_withdraw >= self._limit_withdraw

        if exceeded_limit:
            print("Operation Failed! Withdrawal amount exceeds limit.")

        elif exceeded_withdraw:
            print("Operation Failed! Maximum daily withdrawal number exceeded.")

        else:
            return super().to_withdraw(value)

        return False

    def __str__(self):
        return f"""\
            Agência:\t{self.agency}
            C/C:\t\t{self.account_number}
            Titular:\t{self.customer.name}
            Saldo:\t\tR$ {self.balance:.2f}
        """

class Historic:
    def __init__(self):
        self._transactions = []

    @property
    def transactions(self):
        return self._transactions

    def add_transaction(self, transaction):
        self._transactions.append(
            {
                "type": transaction.__class__.__name__,
                "value": transaction.value,
                "date": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )
    
    def generate_report(self, type_transaction=None):
        for transaction in self._transactions:
            if type_transaction is None or transaction["type"].lower() == type_transaction.lower():
                yield transaction
    
    def transaction_day(self):
        current_date = datetime.itcnow().date()
        transactions = []
        for transaction in self._transactions:
            transaction_date = datetime.strptime(transaction["date"], "%d-%m-%Y %H:%M:%S").date()
            if current_date == transaction_date:
                transactions.append(transaction)
            return transactions


class Transaction(ABC):
    @property
    def value(self):
        pass

    @classmethod
    def register(self, account):
        pass

class Withdral(Transaction):
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    def register(self, account):
        successful_transaction = account.to_withdraw(self.value)

        if successful_transaction:
            account.historic.add_transaction(self)

class Deposit(Transaction):
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    def register(self, account):
        successful_transaction = account.deposit(self.value)

        if successful_transaction:
            account.historic.add_transaction(self)

def log_trasaction(func):
    pass

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDeposit
    [w]\tWithdraw
    [e]\tExtract
    [na]\tNew Account
    [la]\tList Account
    [nu]\tNew User
    [x]\tExit
    => """
    return input(textwrap.dedent(menu))

def filter_customer(cpf, customers):
    filtered_clients = [customer for customer in customers if customer.cpf == cpf]
    return filtered_clients[0] if filtered_clients else None

def recover_customer_account(customer):
    if not customer.accounts:
        print("\n Customer does not have an account!")
        return

    return customer.accounts[0]

@log_trasaction
def deposit(customer):
    cpf = input("Enter the customer's CPF: ")
    customer = filter_customer(cpf, customer)

    if not customer:
        print("\n Customer not found!")
        return

    value = float(input("Enter the amount of your deposit: "))
    transaction = Deposit(value)

    account = recover_customer_account(customer)
    if not account:
        return

    customer.carry_out_transaction(account, transaction)
    
    print(f"Deposit made successfully, in the amount of R$: {value:.2f}")

@log_trasaction
def to_withdraw(customer):
    cpf = input("Enter the customer's CPF: ")
    customer = filter_customer(cpf, customer)

    if not customer:
        print("\n Customer not found!")
        return

    value = float(input("Enter the withdrawal amount: "))
    transaction = Withdral(value)

    account = recover_customer_account(customer)
    if not account:
        return

    customer.carry_out_transaction(account, transaction)

@log_trasaction
def display_extract(customers):
    cpf = input("Enter the customer's CPF: ")
    customer = filter_customer(cpf, customers)

    if not customer:
        print("\n Customer not found!")
        return

    account = recover_customer_account(customer)
    if not account:
        return

    print("\n================ EXTRACT ================")
    transactions = account.historic.transactions

    extract = ""
    if not transactions:
        extrato = "No movements were carried out."
    else:
        for transaction in transactions:
            extract += f"\n{transaction['type']}:\n\tR$ {transaction['value']:.2f}"

    print(extract)
    print(f"\nBalance:\n\tR$ {account.balance:.2f}")
    print("==========================================")

@log_trasaction
def create_customer(customers):
    cpf = input("Enter the customer's CPF (number only): ")
    customer = filter_customer(cpf, customers)

    if customer:
        print("\n There is already a customer with this CPF!")
        return

    name = input("Enter you full name: ")
    birth_date = input("Enter date of birth, in format (dd-mm-aaaa): ")
    address = input("Enter your address (logradouro, nro - bairro - cidade/sigla estado): ")

    customer = PhysicalPerson(name=name, birth_date=birth_date, cpf=cpf, address=address)

    customers.append(customer)

    print("\n  Client created successfully!")

@log_trasaction
def create_account(account_number, customers, accounts):
    cpf = input("Enter the customer's CPF: ")
    customer = filter_customer(cpf, customers)

    if not customer:
        print("\n Customer not found, account creation flow closed!")
        return

    account = CurrentAccount.new_account(customer=customer, account_number=account_number)
    accounts.append(account)
    customer.accounts.append(account)

    print("\n Account created successfully!")

def list_accounts(accounts):
    for account in accounts:
        print("=" * 100)
        print(textwrap.dedent(str(account)))


def main():
    customer = []
    accounts = []

    while True:
        opcao = menu()

        if opcao == "d":
            deposit(customer)

        elif opcao == "w":
            to_withdraw(customer)

        elif opcao == "e":
            display_extract(customer)

        elif opcao == "nu":
            create_customer(customer)

        elif opcao == "na":
            account_number = len(accounts) + 1
            create_account(account_number, customer, accounts)

        elif opcao == "la":
            list_accounts(accounts)

        elif opcao == "x":
            break

        else:
            print("\n Invalid operation, please select the desired operation again.")


main()