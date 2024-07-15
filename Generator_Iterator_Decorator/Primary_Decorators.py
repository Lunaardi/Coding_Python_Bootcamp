def meu_decorador(funcao):					
	def envelope():
		print("Faz algo antes de executar a função.")
		funcao()
		print("Faz algo depois de executar a função.")
								
	return envelope
							
def ola_mundo():
	print("Olá mundo!")


# Para decorar uma funcao em Python, atribuimos a função a um novo valor(argumento)					
ola_mundo = meu_decorador(ola_mundo)

ola_mundo()