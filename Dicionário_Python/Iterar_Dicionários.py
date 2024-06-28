# Exemplo:

contatos = {
	"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
	"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
	"lunaardi@gmail.com": {"nome": "Lunaardi", "telefone": "5846-7895"},
	"julia@gmail.com": {"nome": "Julia", "telefone": "3698-7766"},
}
					
#for chave in contatos:
#	print(chave, contatos[chave])
# >>>
#guilherme@gmail.com {'nome': 'Guilherme', 'telefone': '3333-2221'}
#giovanna@gmail.com {'nome': 'Giovanna', 'telefone': '3443-2121'}
#lunaardi@gmail.com {'nome': 'Lunaardi', 'telefone': '5846-7895'}
#julia@gmail.com {'nome': 'Julia', 'telefone': '3698-7766'}

							
# Exemplo utilizando items 
					
for chave, valor in contatos.items():
	print(chave, valor)
							
#"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
#"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"}
#"lunaardi@gmail.com": {"nome": "Lunaardi", "telefone": "5846-7895"}
#"julia@gmail.com": {"nome": "Julia", "telefone": "3698-7766"}