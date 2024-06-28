# Exemplo: 
					
contatos = {
	"lunaardi@gmail.com": {"nome": "Lunardi", "telefone": "5846-7895"}
}
					
resultado = contatos.pop("lunaardi@gmail.com")
print(resultado)
	# >>> {'nome': 'Lunardi', 'telefone': '5846-7895'}
					
resultado = contatos.pop("lunaardi@gmail.com", {})
print(resultado)
    # >>> {}

resultado = contatos.pop("lunaardi@gmail.com", "não encontrou")
print(resultado)
    # >>> {}