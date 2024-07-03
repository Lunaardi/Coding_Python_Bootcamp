class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento
        
    @property
    def nome(self):
        return self._nome
    
    # @nome.setter
    # def nome(self):
    #     #logica para modificar o nome
    #     pass
        
    
    @property
    def idade(self):
        _ano_atual = 2024
        return _ano_atual - self._ano_nascimento
    
# codigo abaixo que também serve porém não é as melhores praticas/conceitos    

    def get_nome(self):
        return self.nome
    
    def get_idade(self):
        return 2024 - self._ano_nascimento
    

    
pessoa = Pessoa("Lunardi", 1988)
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")

# Exemplo de retorno do codigo get
print(f"Nome: {pessoa.get_nome()} \tIdade: {pessoa.get_idade()}")

# Em Python não tem keyword para fazer encapsulamento, ele faz por convenção.

