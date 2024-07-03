class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        #self.nro_patas = nro_patas # removido por usar keyargs
        self.cor_pelo = cor_pelo
        super().__init__(**kw)
        
    # def __str__(self):
    #     # return self.__class__.__name__  # retorna o nome da classe no caso do ornitorrinco
    #     return "Mamifero"

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        #self.nro_patas = nro_patas  # removido por usar keyargs
        self.cor_bico = cor_bico
        super().__init__(**kw)
        
    # def __str__(self):
    #     return "Aguia de Rapina"

class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

class FalarMixin: # Exerce um retorno que não precisa de ordem de leitura, pois não há outras funções a puxar
    def falar(self):
        return "Olá eu posso falar com você!"

class Ornitorrinco(Mamifero, Ave, FalarMixin):
    def __init__(self, cor_bico, cor_pelo, nro_patas):
        #print(Ornitorrinco.__mro__)    #exemplo 1: mro traz o metodo que o Python executa a leitura das classes herdadas 
        #print(Ornitorrinco.mro())       #exemplo 2: mro traz o metodo que o Python executa a leitura das classes herdadas 
        
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, nro_patas=nro_patas)
        
    # def __str__(self):
    #     return "Ornitorrinco"


cachorro = Cachorro(nro_patas=4, cor_pelo="Caramelo")
print(cachorro)

gato = Gato(nro_patas=4, cor_pelo="Branco")
print(gato)

leao = Leao(nro_patas=4, cor_pelo="Castanho")
print(leao)

ornitorrinco = Ornitorrinco(nro_patas=2, cor_pelo="Vermelho", cor_bico="Laranja") # quando utilizar key args precisamos ajustar os argumentos por chave valor.
print(ornitorrinco)
print(ornitorrinco.falar())
