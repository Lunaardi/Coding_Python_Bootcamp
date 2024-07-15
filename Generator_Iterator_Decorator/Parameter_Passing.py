def mensagem(nome):
    print('executando mensagem')
    return f'Oi {nome}'

def mensagem_longa(nome):
    print('executando mensagem longa')
    return f'Olá tudo bem com você {nome}?'

#def executar(funcao): # veja print 1
#    print('Executando executar')
#    return funcao("Lunardi") # Martelando o Guilherme o código funciona

def executar(funcao, nome): # se eu passar que essa função recebe o campo nome ai podemos passar a variavel "nome" no retorno e executar o nome do print, veja print 2
    print('Executando executar')
    return funcao(nome)

# print(executar(mensagem)) # print 1
print(executar(mensagem, 'Paulo Lunardi')) # print 2
print(executar(mensagem_longa, 'Paulo Lunardi')) # print 2