class Passaro:
	def voar(self):
		print("Passaro Voando")
					
class Pardal(Passaro):
	def voar(self):
		super().voar()
						
class Avestruz(Passaro):
	def voar(self):
		print("Avestruz não consegue voar!")
  
class Tucano(Passaro):
	def voar(self):
		super().voar()
		# print("Tucano esta voando!")

class Marreco(Passaro):
	def voar(self):
		print("Marreco não voa!")

# FIXME: Exemplo de caso a parte, (RUIM) do uso da herança para ganhar o método voar como estudo 
class Aviao(Passaro):
	def voar(self):
		print("Avião esta decolando!")
	
def plano_de_voo(obj):
	obj.voar()
					

p1 = Pardal()
p2 = Avestruz()
p3 = Tucano()
p4 = Marreco()

plano_de_voo(p1)
plano_de_voo(p2)
plano_de_voo(p3)
plano_de_voo(p4)
plano_de_voo(Aviao())
