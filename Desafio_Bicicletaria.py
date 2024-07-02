#Nosso Primeiro Programa POO
				
#			- João tem uma bicicletaria e gostaria de registrar as vendas de suas bicicletas.
#			- Crie um programa onde João informe: cor, modelo, ano e valor da bicicleta vendida.
#			- Uma bicicleta pode: buzinar, parar e correr.
#			- Adicione esses comportamentos!

class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo 
        self.ano = ano 
        self.valor = valor

# abaixo estamos definindo os comportamentos para a classe acima.
# os comportamentos são definidos por metodos e os metodos devem conter um "def" um nome para o metodo.
# dentro do metodo precisamos definir pelo menos 1 argumento, que apra este caso usaremos o "self"
# o "self" é explicito como um argumento posicional, veja o exemplo em b2, sem o self, mas especificando como b2

    def buzinar(self):
        print("Plin...Pliinn")
        
    def parar(self):
        print("Parando Bicicleta...")
        print("Bicicleta parada!")
        
    def correr(self):
        print("Vrummmmmmmmmmm")
        
    def get_cor(self):
        return self.cor
    
    def trocar_marcha(self, nro_marcha):
        print("Trocando Marchaa...")
        
        def _trocar_marcha():
            if nro_marcha > self.marcha:
                print("Marcha trocada...")
            else:
                print("Não foi possivel trocar de Marcha!")
    
    #def __str__(self):
    #    return f"Bicicleta: {self.cor}, {self.modelo}, {self.ano}, {self.valor}"
    #    return f"Bicicleta: cor:{self.cor}, modelo:{self.modelo}, ano={self.ano}, valor={self.valor}" # este caso tras legenda para o retorno
    
    def __str__(self):
       #return f"{self.__class__.__name__}: {[f'{chave}={valor}' for chave, valor in self.__dict__.items()]}" # este caso traz o retorno entre colchetes(lista) para remover utilize o modelo abaico utilizando o join para concatener com "," e espaço
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    
'''
b1 = Bicicleta("vermelho", "caloi_Xs", 2024, 2300)
b1.buzinar()
b1.parar()
b1.correr()
print (b1.cor, b1.modelo, b1.ano, b1.valor)
'''

b2 = Bicicleta("verde", "monark", 2022, 1800)
b2.buzinar() # Bicicleta.buzinar(b2)
print(b2.get_cor())
print(b2) # este metodo trás o caminho do objeto e não a reporesentação do valores que contem para isso usamos o def string, comente o def str e veja a diferença
b2.correr()
