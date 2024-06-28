# Exemplo:
				
contatos = {
	"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
	"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
	"lunardi@gmail.com": {"nome": "Lunardi", "telefone": "5846-7895"},
	"julia@gmail.com": {"nome": "Julia", "telefone": "3698-7766"},
}
					
del contatos["guilherme@gmail.com"]["telefone"]
del contatos["lunardi@gmail.com"]

print(contatos)