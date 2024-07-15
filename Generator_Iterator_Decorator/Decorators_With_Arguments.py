def meu_decorador(funcao):					
	def envelope(*args, **kwargs):
		print("Faz algo antes de executar a função.")
		funcao(*args, **kwargs)
		print("Faz algo depois de executar a função.")
								
	return envelope


@meu_decorador					
def ola_mundo(nome, outro_argumento):
	print(f"Olá mundo {nome}!")


ola_mundo("Lunardi", 1000)