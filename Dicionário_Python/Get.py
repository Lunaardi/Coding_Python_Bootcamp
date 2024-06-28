# Exemplo:
					
contatos = {
	"lunaardi@gmail.com": {"nome": "Lunaardi", "telefone": "5846-7895"}
}
						
# contatos["chave"]
# >>> KeyError: 'chave'
						
print(contatos.get("chave"))
	# >>> None					

print(contatos.get("chave", {}))
	# >>> {}
							
contatos.get("lunaardi@gmail.com", {})
print(contatos)
	# >>> {"lunaardi@gmail.com": {"nome": "Lunaardi", "telefone": "5846-7895"}}

