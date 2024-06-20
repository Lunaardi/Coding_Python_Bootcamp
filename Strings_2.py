nome = "Paulo"
sobrenome = "Lunardi"
idade = 35
profissao = "Programador"
linguagem = "Python"
saldo = 45.4358742098655

pessoa = {"nome": "Paulo", "sobrenome": "Lunardi", "idade": 35, "profissao": "Programador", "linguagem": "Python", "saldo": 45.435}

# Old Style
print("Olá me chamo %s %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." % (nome, sobrenome, idade, profissao, linguagem))

# Método Format
print("Olá me chamo {} {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.".format(nome, sobrenome, idade, profissao, linguagem))
print("Olá me chamo {3} {4}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}.".format(linguagem, profissao, idade, nome, sobrenome))					
print("Olá me chamo {nome} {sobrenome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(nome=nome, sobrenome=sobrenome, idade=idade, profissao=profissao, linguagem=linguagem))
print("Olá me chamo {nome} {sobrenome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(**pessoa))

# Método F-String
print(f"Olá me chamo {nome} {sobrenome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")

# Formatar Strings com f-strings
print(f"Nome: {nome}, Idade: {idade}, Saldo: {saldo:.2f}")
print(f"Nome: {nome}, Idade: {idade}, Saldo: {saldo:10.2f}")
print(f"Nome: {nome}, Idade: {idade}, Saldo: {saldo:15.5f}")