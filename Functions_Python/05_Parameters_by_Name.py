# Keyword only: Exemplo
			
def criar_carro(*,modelo, ano, placa, marca, motor, combustivel):
	print(modelo, ano, marca, motor, combustivel)
						
				
criar_carro(modelo="Kia", ano=2016, placa="ADC-1177", marca="Chevrolet", motor="1.6", combustivel="Gasolina") 	# >>> válido				
#criar_carro("Kia", 2016, "ADC-1177", marca="Chevrolet", motor="1.6", combustivel="Gasolina") 					# >>> inválido
				
# Keyword and Positional only: Exemplo
			
def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
	print(modelo, ano, marca, motor, combustivel)
						
criar_carro("Kia", 2016, "ADC-1177", marca="Chevrolet", motor="1.6", combustivel="Gasolina")				# >>> válido
#criar_carro(modelo="Kia", ano=2016, placa="ADC-1177", marca="Chevrolet", motor="1.6", combustivel="Gasolina") 	# >>> inválido