
# Example 1 - With error
"""
class FileIterator:
	def __init__(self, filename):
		self.file = open(filename)
								
	def __iter__(self):
		return self
								
	def __next__(self):
		line = self.file.readline()
		if line != '':
			return line
		else:
			self.file.close()
			raise StopIteration
									
# Uso do FileIterator
for line in FileIterator('large_file.txt'):
    print(line)
"""
        
# Example 2

class MyIterator:
    def __init__(self, numeros: list[int]):
        self.numeros = numeros
        self.contador = 0
    def __iter__(self):
        return self

    def __next__(self):
        try:
            numero = self.numeros[self.contador] 
            self.contador += 1  # essa função significa que na proxima vez que o codigo retornar ele pega o proximo objeto passado como argumento
            return numero * 2   # agora ele pega o objeto e multiplica pelo valor indicado
        except IndexError:      # esse index error ele vai ignorar caso não tenha um quarto elemento de argumento por exemplo
            raise StopIteration    
    
for i in MyIterator(numeros=[7, 11, 41]):
    print(i)