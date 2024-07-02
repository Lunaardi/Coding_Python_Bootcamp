class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
        
    def __del__(self):
        print("Removendo a Instância da Classe.")    
    
    def falar(self):
        print("Auauu")
        
def criar_cachorro():
    c = Cachorro("Zeus", "Branco e Preto", False)
    print(c.nome)
        
c = Cachorro("Chappie", "Caramelo")
c.falar()

# criar_cachorro()

print("Ola Mundo")
print("Ola Mundo")
del c # este comando é para quando eu desejar remover a classe antes do fim do código
print("Ola Mundo")
print("Ola Mundo")
print("Ola Mundo")
