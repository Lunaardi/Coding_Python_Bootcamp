# Exemplo: 
					
contatos = {
	"lunaardi@gmail.com": {"nome": "Lunardi", "telefone": "5846-7895"}
}
					
print(contatos.popitem())
	# >>> ('lunaardi@gmail.com', {'nome': 'Lunardi', 'telefone': '5846-7895'}
					
print(contatos.popitem())
    # >>> KeyError: 'popitem(): dictionary is empty'