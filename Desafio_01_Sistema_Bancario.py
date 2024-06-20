menu = """

[d] Deposit
[w] Withdraw
[e] Extract
[o] To_Go_Out

=="""

balance = 0
limit = 500
extract = ""
number_withdraw = 0
LIMIT_WITHDRAW = 3

while True:

    option = input(menu)

    if option == "d":
        value = float(input("Enter the deposit amount: "))
        
        if value > 0:
            balance += value
            extract += f"depósito: R$ {value:.2f}\n"
            print(f"Deposit made successfully, in the amount of R$: {value:.2f}")

        else: print("Operation Failed! The value entered is invalid.")

    elif option == "w":
        value = float(input("Enter the whithdraw amount: "))

        exceeded_balance = value > balance

        exceeded_limt = value > limit

        exceeded_withdraw = number_withdraw >= LIMIT_WITHDRAW

        if exceeded_balance:
            print("Operation Failed! You don't have enough balance.")

        elif exceeded_limt:
            print("Operation Failed! Withdrawal amount exceeds limit.")

        elif exceeded_withdraw:
            print("Operation Failed! Maximum daily withdrawal number exceeded.")

        elif value> 0:
            balance -= value
            extract += f"saque: R$ {value:.2f}\n"
            number_withdraw += 1
            print(f"withdrawal in the amount of R$: {value:.2f} made successfully, your current balance is: R$ {balance:.2f}")

        else:
            print("Operation Failed! The value entered is invalid.")

    elif option == "e":
        print("\n==================== EXTRACT ====================")
        print("No transactions were made on your account." if not extract else extract)
        print(f"\nBalance: R$ {balance:.2f}")
        print("==================================================")

    elif option == "o":
        break

    else:
        print("Operation Invalid! Please select the desired selection again")
