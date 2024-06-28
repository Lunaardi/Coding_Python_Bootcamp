# Exemplo: 
					
contatos = {
	"lunaardi@gmail.com": {"nome": "Lunardi", "telefone": "5846-7895"}
}
print(contatos)
					
contatos.update({"lunaardi@gmail.com": {"nome", " Paulo Lunardi"}})
print(contatos)
	# >>> {"lunaardi@gmail.com": {"nome", "Paulo Lunardi")}
					
contatos.update({"gionanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"}})
print(contatos)
	# >>> {'lunaardi@gmail.com': {'nome', 'Paulo Lunardi'}, ' gionanna@gmail.com': {"nome", "Giovanna", "telefone": "3443-2121"}}