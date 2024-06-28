# Exemplo de variavel com Escopo Global:
				
salario = 2000
					
def salario_bonus(bonus):
	global salario
	salario += bonus
	return salario
						
salario_atual = salario_bonus(500) 
print(f"Seu salario atual é R$: {salario_atual}")
    # >>> 2500


