from abc import ABC, abstractmethod

class ControleRemoto(ABC):  
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

# Decorador: onde todas as classes filhas de controle remoto tem que implrementar a @property
# Decorador: onde todas as classes filhas de controle remoto tem que implrementar a @property + @abstractpropert
    @property
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print("Lingando a Televisão!")
        print("Televisão Ligada!")
        
    def desligar(self):
        print("Desligando a Televisão!")
        print("Televisão Desligada!")
    
    @property
    def marca(self):
        return "LG"
        
class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o Ar Condicionado!")
        print("Ar Condicionado Ligado!")
        
    def desligar(self):
        print("Desligando o Ar Condicionado!")
        print("Ar Condicionado Desligado!")
        
    @property 
    def marca(self):
        return "Philco"
        
class AbrirPortao(ControleRemoto):
    def ligar(self):
        print("Abrindo o Portão!")
        print("Portão aberto!")
        
    def desligar(self):
        print("Fechando o Portão!")
        print("Portão Fechado!")
        
    @property 
    def marca(self):
        return "Honda"

controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)

controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)

controle = AbrirPortao()
controle.ligar()
controle.desligar()
print(controle.marca)

# Nome metodo abstrato significa que a classe não vai ter um corpo, e todas as classes filhas são obrigadas a implementar.
# uma vez que tenho um método abstrato uma classe se torna abstrata, significa que ela não pode ser instanciada diretamente.
