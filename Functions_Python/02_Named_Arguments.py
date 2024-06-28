# Exemplo:
				
def salvar_carro(marca, modelo, ano, placa):
#def salvar_carro(ano, modelo, marca, placa):
	#salva carro no banco de dados..
	print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")
					
salvar_carro("Kia", "sportage", 2016, "ADC-1177" ) 
    # Desvantagem, caso o usuário inverta a sequencia dos argumentos de dados.
salvar_carro(marca="Chevrolet", modelo="cruise", ano="2014", placa="ADF-3345")
salvar_carro(**{"marca": "Chevrolet", "modelo": "cruise", "ano": 2014, "placa": "ADF-3345"})
	# Esses 2 "*" significa que estou passando um dicionario para esta função
	# Carro inserido com sucesso! Kia/sportage/2016/ADC-1177