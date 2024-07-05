# Atributos_de_Classe_ou_Instancia

class Estudante:
    escola = "DIO" # variavel de classe
    
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula # variavel de intância
        
    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"
    
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)
    
aluno_1 = Estudante("Lunardi", 1)
aluno_2 = Estudante("Giovanna", 2)
aluno_3 = Estudante("Backes", 3)
mostrar_valores(aluno_1, aluno_2)


Estudante.escola = "Nearx"          # variavel de classe
# aluno_1.matricula = 3               # variavel de intância

aluno_3 = Estudante("Backes", 3)
mostrar_valores(aluno_1, aluno_2, aluno_3)   
