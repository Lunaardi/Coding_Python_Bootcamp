class Foo:                          # criando uma classe
    def __init__(self, x=None):     # construtor
        self._x = x                 # definie uma variavel privada x
   
    @property                       #verifique que quando comentamos esta linha o def perde a referencia e trás o local ao invés da variavel privada definida
    def x(self):                    # Define uma variavel que se chama x
        return self._x or 0
    
    @x.setter
    def x(self, value):
        self._x += value
        # return self._x + value # este modelo ele substitui ao inves de adicionar a variavel ao valor adicionado
        
    @x.deleter
    def x(self):
        self._x = 0
        #del self._x
    
foo = Foo(10)
print(foo.x)
foo.x = 10
print(foo.x)
del foo.x
print(foo.x)
