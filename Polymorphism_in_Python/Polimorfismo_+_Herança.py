class Passaro:
	def voar(self):
		pass
					
class Pardal(Passaro):
	def voar(self):
		print("Pardal esta voando!")
						
class Avestruz(Passaro):
	def voar(self):
		print("Avestruz não voa!")
  
class Tucano(Passaro):
	def voar(self):
		print("Tucano esta voando!")
  
class Marreco(Passaro):
	def voar(self):
		print("Marreco não voa!")
						
def plano_de_voo(passaro):
	passaro.voar()
					
# Exemplo 1:     
# Este exemplo de chamar a função do objeto pode ser substituida pelo exemplo 2
# plano_de_voo(Pardal())
# plano_de_voo(Avestruz())
# plano_de_voo(Tucano())

p1 = Pardal
p2 = Avestruz
p3 = Tucano
p4 = Marreco

plano_de_voo(p1)
plano_de_voo(p2)
plano_de_voo(p3)
plano_de_voo(p4)
