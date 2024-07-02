import textwrap

def menu():
    menu = """\n
    ==================== MENU ====================
    [d]\tDeposit
    [w]\tWithdraw
    [e]\tExtract
    [na]\tNew account
    [la]\tList accounts
    [nu]\tNew user
    [o]\tTo_Go_Out
    ==> """
    return input(textwrap.dedent(menu))

def deposit(balance, value, extract, /):
    if value > 0:
        balance += value
        extract += f"depósito: R$ {value:.2f}\n"
        print(f"Deposit made successfully, in the amount of R$: {value:.2f}")
    else:
        print("Operation Failed! The value entered is invalid.")
    
    return balance, extract
        
def withdraw(*, balance, value, extract, limit, number_withdraw, limit_withdraw):
        exceeded_balance = value > balance
        exceeded_limt = value > limit
        exceeded_withdraw = number_withdraw >= limit_withdraw

        if exceeded_balance:
            print("Operation Failed! You don't have enough balance.")

        elif exceeded_limt:
            print("Operation Failed! Withdrawal amount exceeds limit.")

        elif exceeded_withdraw:
            print("Operation Failed! Maximum daily withdrawal number exceeded.")

        elif value > 0:
            balance -= value
            extract += f"Saque:\t\tR$ {value:.2f}\n"
            number_withdraw += 1
            print(f"withdrawal in the amount of R$: {value:.2f} made successfully, your current balance is: R$ {balance:.2f}")

        else:
            print("Operation Failed! The value entered is invalid.")
        
        return balance, extract, number_withdraw
    
def show_extract(balance, /, *, extract):
    print("\n==================== EXTRACT ====================")
    print("No transactions were made on your account." if not extract else extract)
    print(f"\nBalance: R$ {balance:.2f}")
    print("==================================================")
     
def create_new_user(users):
    cpf = input("Enter your CPF! (only numbers): ")
    user = filter_user(cpf,users)
    
    if user:
        print("\n There is already a user related to this CPF! ")
        return
    
    name = input("Enter your full name: ")
    date_of_birth = input("Enter your date of birth in the format (dd-mm-yyyy): ")
    address = input("Enter yout address(public place, number - district - city/state acronym): ")
    
    users.append({"name": name, "date_of_birth": date_of_birth, "cpf": cpf, "address": address})
    
    print(" ======== User registration created successfully ========")
    
def filter_user(cpf, users):
    users_filtered = [user for user in users if user["cpf"] == cpf]   # verifica se o usuario que eu estou percorrendo no momento, se o cpf dele é igual ao informado, se for ele traz um numero de retorno, se não a lista fica vazia.
    return users_filtered[0] if users_filtered else None            # verifica se o usuario filtrado for um lista vazia, ele retorna o primeiro elemento. Pois não se pode cadastrar 2 usuarios a um mesmo cpf.
 
def create_account(bank_agency, number_account, users):
    cpf = input("Enter the user's CPF: ")
    user = filter_user(cpf, users)
    
    if user:
        print("\n=== New account created successfully! ===")
        return {"bank_agency": bank_agency, "number_account": number_account, "user": user}
    
    print("\n=== User not found, account creation flow closed! ===")
    
def list_accounts(accounts):
    for account in accounts:
        linha = f"""\
            Agency:\t{account['bank_agency']}
            C/C:\t{account['number_account']}
            Holder:\t{account['user']['name']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMIT_WITHDRAW = 3
    BANK_AGENCY = "0001"
    
    balance = 0
    limit = 500
    extract = ""
    number_withdraw = 0
    users = []
    accounts = []
    
    while True:
        option = menu()
        
        if option == "d":
            value = float(input("Enter the deposit amount: "))
            
            balance, extract = deposit(balance, value, extract)
        
        elif option == "w":
            value = float(input("Enter the whithdraw amount: "))
            
            balance, extract, number_withdraw = withdraw(
                balance=balance,
                value=value,
                extract=extract,
                limit=limit,
                number_withdraw=number_withdraw,
                limit_withdraw=LIMIT_WITHDRAW,
            )
            
        elif option == "e":
            show_extract(balance, extract=extract)
            
        elif option == "nu":
            create_new_user(users)
            
        elif option == "na":
            number_account = len(accounts) + 1
            account = create_account(BANK_AGENCY,number_account, users)
            
            if account:
                accounts.append(account)

        elif option == "la":
            list_accounts(accounts)
        
        elif option == "o":
            break

        else:
            print("Operation Invalid! Please select the desired selection again")

main()
