def sacar(valor):
    saldo = 1000


    if saldo >= valor:
        print("Valor Sacado!")
        print("Retire seu dinheiro na boca do caixa!")
        print(f"Seu saldo atual é de {saldo - valor} reais")


def depositar(valor):
    saldo = 1000.0
    saldo += valor
    if valor > 0:
        print(f"Deposito realizado, valor atual de {saldo}")


#sacar(200)
depositar(1000)