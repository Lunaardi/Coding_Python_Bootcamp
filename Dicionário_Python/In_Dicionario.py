# Exemplo:
				
contatos = {
	"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
	"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
	"lunaardi@gmail.com": {"nome": "Lunardi", "telefone": "5846-7895"},
	"julia@gmail.com": {"nome": "Julia", "telefone": "3698-7766"},
}
					
resultado = "guilherme@gmail.com" in contatos			# >>> True
print(resultado)

resultado1 = "megui@gmail.com" in contatos              # >>> False
print(resultado1)
					
resultado2 = "idade" in contatos["guilherme@gmail.com"]  # >>> False
print(resultado2)

resultado3 = "telefone" in contatos["giovanna@gmail.com"] # >>> True
print(resultado3)

#caso não houvesse o "in" este seria o processo utilizado para verificar as chaves

#lista_chaves: list = contatos.keys()
#print(lista_chaves)

#index = lista_chaves.count("guilherme@gmail.com")
#print(index)
