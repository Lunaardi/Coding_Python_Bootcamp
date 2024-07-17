from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    with open(ROOT_PATH / "1lorem.txt", "r") as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(f"Erro ao abrir o arquivo {exc}")
    
        

# Example 2
# from pathlib import Path

# ROOT_PATH = Path(__file__).parent

# # com essa forma validamos que o arquivo foi fechado, apagando as variaveis da memória
# with open(ROOT_PATH / "lorem.txt", "r") as arquivo:
# #    print("Trabalhando com o arquivo")
# #    1 / 0
    
# print(arquivo.read())