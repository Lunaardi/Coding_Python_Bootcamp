# Example 1
def meu_gerador1():
    yield 1

for i in meu_gerador1():
    print(i)
    
# Example 2
def meu_gerador2():
    texto = "Python"
    yield texto

for o in meu_gerador2():
    print(o)
    
# Example 3
def my_generator(numeros: list[int]):
    for numero in numeros:              # Metodo para gerar um contador 
        yield numero * 2                # continuação do contador acima

for n in my_generator(numeros=[2, 8, 16]):
    print(n)
    
# Example 4
def my_generator(numeros: list[int]):
    return numeros * 2
    yield numeros #my_generator

for n in my_generator(numeros=[2, 8, 16]):
    print(n)
    
    
    
    
    

    