# Case example 1
"""
def duplicar(func):
	def envelope(*args, **kwargs):
		func(*args, **kwargs)
		return func(*args, **kwargs)
								
	return envelope
							
@duplicar
def aprender(tecnologia):
	print(f"estou aprendendo {tecnologia}")
	return tecnologia.upper()
							
tecnologia = aprender("Python")
print(tecnologia)
"""

# Case example 2
def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print("faz algo antes de executar")
        resultado = funcao(*args, **kwargs)
        print("faz algo depois de executar")
        return resultado
    
    return envelope

@meu_decorador
def ola_mundo(nome, argumento_kwars):
    print(f"Olá mundo ({nome}!")
    return nome.upper()

resultado = ola_mundo("Lunardi", 11000)
print(resultado)

