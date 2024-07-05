# Método_de_Classe_ou_Estático.py

class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
    
    @classmethod
    #1 def criar_de_data_nascimento(self, ano, mes, dia, nome):
    def criar_de_data_nascimento(cls, ano, mes, dia, nome): # invoca o nome do método no caso "Pessoa"
        #1 print(cls)
        idade = 2024 - ano
        return cls(nome, idade)
    
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18
    
# p = Pessoa("Lunardi", 35)
# print(p.nome, p.idade)

# Nesta etapa primeiro ele cria uma instancia "Pessoa()" e depois executa o objeto
# p = Pessoa().criar_de_data_nascimento(1988, 8, 13, "Lunardi" ) 

p = Pessoa.criar_de_data_nascimento(1988, 8, 13, "Lunardi") # Desta maneira não criamos uma instância o que seria a melhor prática em Python
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))
