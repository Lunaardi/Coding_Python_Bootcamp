import functools

def meu_decorador(funcao):
        @functools.wraps(funcao) #neste decorador passar a função que recebemos por argumento, ou seja ela trás o nome correto da função
        def envelope(*args, **kwargs):
            funcao(*args, **kwargs)
            
        return envelope
    
@meu_decorador
def ola_mundo(nome, argumento_kwars):
    print(f"Olá mundo ({nome}!")

print(ola_mundo.__name__)