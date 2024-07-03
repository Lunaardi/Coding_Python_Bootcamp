class Veiculo:
    def __init__(self, cor, placa, nro_chassi):
        self.cor = cor
        self.placa = placa
        self.nro_chassi = nro_chassi
        
    def ligar_motor(self):
        print("Ligando o Motor")
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"
    
    
class Motocicleta(Veiculo):
    pass
    
class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, nro_chassi, carregado):
        super().__init__(cor, placa, nro_chassi)
        self.carregado = carregado
        
    def esta_carregado(self):
        print(f"{'Sim estou carregado' if self.carregado else 'Não estou carregado'}")
        
        
    
moto = Motocicleta("Preto", "ACD-1177","5554844856")
#moto.ligar_motor()

carro = Carro("Branco", "OFD-2255","7795632468")
#carro.ligar_motor()
# carro.esta_carregado() # nesta caso a função esta carregado não esta atribuida neste escopo

caminhao = Caminhao("Verde", "SDF-6598","9956345585", True)
#caminhao.ligar_motor()

print(moto)
print(carro)
print(caminhao)
