# Example 1: filtro

numeros = [1, 30, 21, 2, 9, 65, 34, 12, 100, 33]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)

# Example 2: filtro

numeros = [1, 30, 21, 2, 9, 65, 34, 91, 22, 73]
pares = [numero for numero in numeros if numero % 2 == 0]

print(pares)

# Example 3: Modificando valores

numeros = [1, 2, 3, 30, 21, 9, 65, 34, 73, 78, 28, 44]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)

print(quadrado)


# Example 4: Modificando valores

numeros = [1, 30, 21, 2, 9, 65, 34, 76, 22, 2, 9]
quadrado = [ numero ** 2 for numero in numeros]

print(quadrado)

