import textwrap
from abc import ABC
from datetime import datetime

# É uma clase que define um cliente que pode realizar transações usando suas contas. 
# A classe tem uma função __init__ que recebe o endereço do cliente como entrada e uma função realizar_transacao que recebe a conta do cliente e a transação com entrada e registramos a transação na conta, retornando None. 
#A função add_account recebe a conta do cliente como entrada e a adiciona à lista de contas do cliente. 
#Essas funções podem ser usadas para rastrear transações e contas do cliente.

class Customer:
    def __init__(self, address):
        self.address = address
        self.accounts = []

    def carry_out_transaction(self, account, transaction):
        transaction.register(account)

    def add_account(self, account):
        self.accounts.append(account)


# Classe PhysicalPerson em Python que estende a classe Customer. 
# A função __init__ recebe o nome, a data de nascimento e o CPF da pessoa como entrada, chama a função __init__ superclasse com o endereço como entrada.
# Depois define as propriedades de nome e data de nascimento do pessoa, bem como a propriedade CPF que é específica para PhysicalPerson.
# A classe PhysicalPerson tem as mesmas funções realizar_transacao e add_account definidas na classe Customer, e pode ser usada para gerenciar transações e adição de contas de pessoas físicas.

class PhysicalPerson(Customer):
    def __init__(self, name, birth_date, cpf, address):
        super().__init__(address)
        self.name = name
        self.birth_date = birth_date
        self.cpf = cpf

# O construtor toma o número da conta e o cliente como entrada e atribui o saldo a 0.
# Atribui o número da conta a uma propriedade apropriada, define o número da agência com o valor padrão de "0011" e atribui o objeto cliente à propriedade apropriada.
# Ele também atribui um objeto Historic à propriedade historic.
#Com essa classe, pode-se gerenciar informações de contas bancárias, como saldo, número da conta, agência e cliente, além de registrar a história de transações relacionadas à cuenta.
class Account:
    def __init__(self, account_number, customer):
        self._balance = 0
        self._account_number = account_number
        self._agency = "0011"
        self._customer = customer
        self._historic = Historic()
			
# Esse é um método de classe Account que cria um objeto account para um cliente específico, tendo como entrada o número da conta e o cliente.
# Ele retorna o objeto account criado.
# O método é definido usando um método de classe @classmethod, o que significa que ele é chamado na classe Account em vez de em um objeto específico do account.
# Isso faz com que seja possível criar uma conta sem precisar criar um objeto account antes.
    @classmethod
    def new_account(cls, customer, account_number):
        return cls(account_number, customer)

#Essa é uma propriedade que retorna o saldo da conta, usando o atributo privtado "_balance". 
    @property
    def balance(self):
        return self._balance

# Essa é uma propriedade que retorna o número da conta, usando o atributo privado "_account_number". 
    @property
    def account_number(self):
        return self._account_number

# Essa é uma propriedade que retorna o nome da agência, usando o atributo privado "_agency". 
    @property
    def agency(self):
        return self._agency

# Essa é uma propriedade que retorna o cliente associado à conta, usando o atributo privado "_customer".
    @property
    def customer(self):
        return self._customer

# Essa é uma propriedade que retorna o historico associado à conta, usando o atributo privado "_historic".
    @property
    def historic(self):
        return self._historic

# Esse é um método da classe Account, chamado to_withdraw, que processa transações de saque. 
# É usado para retirar dinheiro de uma conta, se houver saldo suficiente, e retorna true se a transação for bem-sucedida, senão false.
# Além disso, ele imprime mensagens de retorno ao usuário para confirmar que a transação foi bem-sucedida ou que ela falhou por falta de saldo.
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

# Esse é um método da classe Account, chamado deposit, que processa transações de depósito.
# É usado para depor dinheiro em uma conta, e retorna True se a transação for bem-sucedida, senão False.
# Além disso, ele imprime mensagens de retorno ao usuário para confirmar que o depósito foi bem-sucedido, e é utilizado para atualizar o saldo da conta.
    def deposit(self, value):
        if value > 0:
            self._balance += value
            print(f"Deposit made successfully!")
            
        else:
            print("Operation Failed! The value entered is invalid.")
            return False

        return True

# Essa é uma classe que herda da classe Account, e adiciona recursos adicionais para uma conta corrente, chamados de limite de saldo e limite de saque. 
# O limite de saldo é o limite de quanto dinheiro pode ser depositado na conta, enquanto o limite de saque é o limite de quantos saques podem ser feitos em um determinado período.
# Esses recursos são definidos ao criar uma nova Account, e podem ser alterados durante a vida da conta.
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

# Método especial do Python que retorna uma representação textual de um objeto. 
# Para essa classe CurrentAccount ele retorna uma string que representa uma conta corrente, com a agência, o número da conta e o nome do titular da conta.
    def __str__(self):
        return f"""\
            Agência:\t{self.agency}
            C/C:\t\t{self.account_number}
            Titular:\t{self.customer.name}
        """

# Essa é uma classe 'Historico', que representa uma lista de transações que aconteceram em uma conta.
# Ela possui um atributo '_transacoes', que é uma lista de dicionários de dados de transação.
# Quando uma nova transação é adicionada à lista, é criado um novo dicionário com as informações da transação, como o tipo da transação, o valor e a data e hora da transação.
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
                "date": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )

# Isso é uma classe que herda da classe Abstract Base Class (ABC), chamada de Transacao. 
# Eles possuem um atributo de propriedade abstrato chamado 'value', que é necessário implementar em qualquer subclasse de Transacao. 
# Eles também tem um método de classe abstrato chamado de 'registrar', que também precisa ser implementado em qualquer subclasse de Transacao.
# Isso significa que qualquer classe que herda Transacao precisa definir uma implementação de valor e registrar para que possa ser usada com sucesso.
class Transaction(ABC):
    @property
    def value(self):
        pass

    @classmethod
    def register(self, account):
        pass

# Essa é uma classe chamada Withdral, que herda da classe Transacion.
# Ela tem um campo privado chamado '_value', que é o valor que o usuário tentou sacar da conta.
# Essa classe também tem um método de classe chamado 'register', que é usado para registrar a transação na lista de transação da conta.
# Se o saque for bem sucedido, ele adiciona a transação à lista de transações, se não, ele retorna False.
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

# Essa é uma classe chamada Deposit, que herda da classe Transacion. 
# Ela tem um campo privado chamado '_value', que é o valor que o usuário tentou depositar na conta.
# Essa classe também tem um método de classe chamado 'register', que é usado para registrar a transação na lista de transação da conta.
# Se o depósito for bem sucedido, ele adiciona a transação à lista de transações, se não, ele retorna False
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

# Isso é um menu interativo que pede que o usuário escolha entre diferentes opções, como 'Depositar', 'Sacar', 'Extrado', 'Nova conta', 'Listar contas', 'Novo usuário' e 'Sair'. 
# O menu é impresso como um string, e a escolha do usuário é feita através da função 'input' e a opção escolhida é guardada em uma variável.
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

# Essa é uma função chamada 'filtrar_cliente', que tem dois parâmetros: cpf, que é o número de identification de um cliente, e clientes, que é uma lista de objetos 'Client', representando uma lista de todos os clientes cadastrados. 
# A função filtra os clientes da lista baseada no cpf fornecido e retorna o primeiro objeto que corresponda ao cpf, ou None se nenhum cliente correspondente for encontrado na lista.
def filter_customer(cpf, customers):
    filtered_clients = [customer for customer in customers if customer.cpf == cpf]
    return filtered_clients[0] if filtered_clients else None

# Essa é uma função chamada 'recover_customer_account', que tem um parâmetro chamado 'customer', que é um objeto representando um cliente.
# A função verifica se o cliente tem uma conta (por meio do atributo 'accounts') e, se não tiver, retorna uma mensagem de erro.
# Se o cliente tiver uma conta, a função retorna o primeiro objeto de 'accounts' (0), que é a primeira conta disponível do cliente.
def recover_customer_account(customer):
    if not customer.accounts:
        print("\n Customer does not have an account!")
        return

    return customer.accounts[0]

# Essa é uma função chamada 'deposit', que tem um parâmetro chamado 'customer', que é um objeto representando um cliente.
# A função começa pedindo o número de identificação do cliente cpf e usa a função 'filter_customer' para filtro os clientes pela cpf fornecido.
# Em seguida, a função verifica se o cliente tem uma conta (por meio do atributo 'accounts') e, se não tiver, retorna uma mensagem de erro.
# Se o cliente tiver uma conta, a função retorna o primeiro objeto de 'accounts' (0), que é a primeira conta available do cliente.
# A função então pega o valor da transação, retorna transação e usa o método 'registrar', que é o método para registrar a transação na conta do cliente.
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

# Essa é uma função chamada 'to_withdraw', que tem um parâmetro chamado 'customer', que é um objeto representando um cliente.
# A função começa pedindo o número de identificação do cliente cpf e usa a função 'filter_customer' para filtro os clientes pela cpf fornecido.
# Em seguida, a função verifica se o cliente tem uma conta (por meio do atributo 'accounts') e, se não tiver, retorna uma mensagem de erro.
# Se o cliente tiver uma conta, a função retorna o primeiro objeto de 'accounts' (0), que é a primeira conta available do cliente.
# A função então pega o valor da transação, retorna transação e usa o método 'registrar', que é o método para registrar a transação na conta do cliente.
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

# Esta é uma função chamada 'display_extract', que tem um parâmetro chamado 'customer', que é um objeto representando um cliente.
# A função começa pedindo o número de identificação do cliente cpf e usa a função 'filter_customer' para filtra os clientes pela cpf fornecido.
# Em seguida, a função verifica se o cliente tem uma conta (por meio do atributo 'accounts') e, se não tiver, retorna uma mensagem de erro.
# Se o cliente tiver uma conta, a função retorna o primeiro objeto de 'accounts' (0), que é a primeira conta available do cliente.
# A função então pega o valor da transação, retorna transação e usa o método 'registrar', que é o método para registrar a transação na conta do cliente.

# A função 'display_extract' então exibe as informações extraídas da conta. 
# A função exibe o nome do cliente, o limite de saque, o limite de depósito, uma lista de transações feitas na conta e o saldo atual da conta.
# Se não houver transações na conta, a função exibe uma mensagem informando que não houve movimentações na conta.
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

# A função create_customer é uma função que cria um novo cliente, a partir da lista de clientes que é fornecida.
# A função começa pedindo o número de identificação do cliente cpf e usa a função 'filter_customer' para filtro os clientes pela cpf fornecido.
# Em seguida, a função verifica se o cliente tem uma conta (por meio do atributo 'accounts') e, se não tiver, retorna uma mensagem de erro.
# Se o cliente tiver uma conta, a função retorna o primeiro objeto de 'accounts' (0), que é a primeira conta available do cliente.
# A função então pega o valor da transação, retorna transação e usa o método 'registrar', que é o método para registrar a transação na conta do cliente.
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

# A função 'create_account' cria uma nova conta para um cliente e adiciona à lista de contas. 
# A função começa pedindo o número de identificação do cliente cpf e usa a função 'filter_customer' para filtro os clientes pela cpf fornecido.
# Em seguida, a função verifica se o cliente tem uma conta (por meio do atributo 'accounts') e, se não tiver, retorna uma mensagem de erro. 
# Se o cliente tiver uma conta, a função retorna o primeiro objeto de 'accounts' (0), que é a primeira conta available do cliente. 
# A função então pega o valor da transação, retorna transação e usa o método 'registrar', que é o método para registrar a transação na conta do cliente.
# A função 'create_account' então cria uma nova conta para o cliente e adiciona à lista de contas.
# É importante notar que esta função será chamada dentro de outra função que gerencia a lista de clientes e contas, com o objetivo de garantir que todas as contas sejam associadas a um cliente.
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

# A função list_accounts é uma função que lista todas as contas da lista 'accounts', a partir das informações de cada conta.
# A função começa com um loop que iterar sobre todas as contas da lista.
# Em cada iteração do loop, a function printa uma linha com 100 caracteres consistindo apenas do caractere "=".
# Em seguida, a função usa o método 'dedent' do módulo 'textwrap' para remover o espaçamento em branco antes da representação de cada conta, para que ela seja impressa com o tamanho exato do objeto.
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
