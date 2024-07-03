class Foo:
	def __init__(self, x=None):
		self._x = x
						
	@property   # decorador é uma função que executa antes da sua função
	def x(self):
		return self._x or 0
						
	@x.setter # processo de atribuição do seu atributo
	def x(self, value):
		_x = self._x or 0
		_value = value or 0
		self._x = _x + _value
						
	@x.deleter # processo de remoção da atribuição do seu atributo
	def x(self):
		self._x = -1
						
foo = Foo(10)
print(foo.x)
foo.x = 10
print(foo.x) # seria esse retorno considerando que o foo + valor ex: self._x = _x + _value
del foo.x
print(foo.x)
