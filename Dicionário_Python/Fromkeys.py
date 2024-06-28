# Exemplo 1: Quando se deseja apenas criar uma variavel sem vincular nenhum valor
					
dict.fromkeys(["nome", "telefone"])
print(dict.fromkeys(["nome", "telefone"]))
	# >>> {"nome": "None", "telefone": "None"}
						
# Exemplo 1: Quando se deseja apenas criar um conjunto de chaves e vincular um valor padrão nelas.
						
dict.fromkeys(["nome", "telefone"], "vazio")
print(dict.fromkeys(["nome", "telefone"], "vazio"))
	# >>> {"nome": "vazio", "telefone": "vazio"}