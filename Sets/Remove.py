# Exemplo:
				
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}					
print(numeros) # >>> {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

numeros.remove(0)
print(numeros) # >>> {1, 2, 3, 4, 5, 6, 7, 8, 9}

numeros.remove(9)
print(numeros) # >>> {1, 2, 3, 4, 5, 6, 7, 8}

numeros.remove(5)
print(numeros) # >>> {1, 2, 3, 4, 6, 7, 8}