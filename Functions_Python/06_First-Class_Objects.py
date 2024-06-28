# Exemplo:
				
def somar(a, b):
	return a + b

def subtrair(a, b):
	return a - b
					
def exibir_resultado(a, b, funcao):
	resultado = funcao(a, b)
	print(f"O resultado da operação é = {resultado}")
	
def exibir_resultado2(a, b, funcao):
	resultado = funcao(a, b)
	print(f"O resultado da operação {a} - {b} = {resultado}")
						
exibir_resultado(10, 10, somar) 
	# >>> O resultado da operação 10 + 10 = 20
	
exibir_resultado2(60, 15, subtrair) 
	# >>> O resultado da operação 60 - 15 = 45

op = somar

print(op(1, 73))
