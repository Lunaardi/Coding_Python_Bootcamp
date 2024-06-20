texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

# exemplo utilizando um interal
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print() # adiciona uma quebra de linha

# exemplo usando range comum
for numero in range(0, 11):
    print(numero, end=" ")

# exemplo usando a função built-in range
for numero in range(0, 51, 5):
    print(numero, end=" ")
