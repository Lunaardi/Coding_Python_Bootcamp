# Exemplo:
				
contatos = {
	"lunaardi@gmail.com": {"nome": "Lunaardi", "telefone": "5846-7895"}
}
					
copia = contatos.copy()
copia["lunaardi@gmail.com"] = {"nome": "Paulo"}

print(contatos["lunaardi@gmail.com"])  	# >>> {"nome": "Lunaardi", "telefone": "5846-7895"}
print(copia["lunaardi@gmail.com"]) 		# >>> {"nome": "Paulo"}