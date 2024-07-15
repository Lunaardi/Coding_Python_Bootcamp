def dizer_oi(nome):
	return f"Oi {nome}"
						
def incentivar_aprender(nome):
	return f"Oi {nome}, vamos aprender Python juntos!"
						
def mensagem_para_guilherme(funcao_mensagem):
	return funcao_mensagem("Guilherme")
						
print(mensagem_para_guilherme(dizer_oi))
print(mensagem_para_guilherme(incentivar_aprender))



