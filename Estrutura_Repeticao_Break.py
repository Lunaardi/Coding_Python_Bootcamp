'''
# Exemplo 1
opcao = -1

while opcao != 0:
    opcao = int(input("Informe um número: "))

    if opcao == 10:
        break

    print(opcao)

# Exemplo 2
while True:
    numero = int(input("Informe um número: "))

    if opcao == 10:
        break

    print(opcao)

# Exemplo 3 - para a execução no numero indicado
for numero in range(100):
    
    if numero == 12:
        break

    print(numero, end=" ")

# Exemplo 4
for numero in range(100):
    
    if numero == 12:
        continue

    print(numero, end=" ")

# Exemplo 5 (quando eu não quero exibir uma classe de numeros, por exemplo numeros pares maior que 2)
for numero in range(100):

    if numero % 2 == 0:
        continue # pula a execução do numero indicado

    print(numero, end= " ")

'''

# Exemplo 6 (continue + break)
while True:
    numero = int(input("Informe o número: "))

    if numero == 10:
        break

    if numero % 2 ==  0:
        continue

    print(numero, end=" ")