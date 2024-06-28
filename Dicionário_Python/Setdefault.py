# Exemplo: 
					
contato = {"nome": "Lunardi", "telefone": "5846-7895"}
					
contato.setdefault("nome", "Giovanne")
print(contato)
# >>> "Lunardi"
					
contato.setdefault("idade", 35)
print(contato)
	# >>> {"nome": "Lunardi", "telefone": "5846-7895", "idade":28}