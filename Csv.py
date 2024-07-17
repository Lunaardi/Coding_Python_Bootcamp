import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent

# Criação do arquivo CSV
# try:
#     with open(ROOT_PATH / "usuarios.csv", 'w', encoding="utf-8") as arquivo:
#         escritor = csv.writer(arquivo)
#         escritor.writerow(["id", "nome"])
#         escritor.writerow(["1", "Lunardi"])
#         escritor.writerow(["2", "Marisa"])
# except IOError as exc:
#     print(f"Erro ao abrir o arquivo. {exc}")


# Leitura do arquivo CSV
# try:
#     with open(ROOT_PATH / "usuarios.csv", 'r', encoding="utf-8") as arquivo:
#         leitor = csv.reader(arquivo)
#         for row in leitor:
#             print(row)
# except IOError as exc:
#     print(f"Erro ao abrir o arquivo. {exc}")


# Leitura do arquivo CSV por coluna
# COLUNA_ID = 0
# COLUNA_NOME = 1


# Normal sem formatação
# try:
#     with open(ROOT_PATH / "usuarios.csv", 'r', newline="", encoding="utf-8") as arquivo:
#         leitor = csv.reader(arquivo)
#         for row in leitor:
#             print(row[COLUNA_ID], row[COLUNA_NOME])
# except IOError as exc:
#     print(f"Erro ao abrir o arquivo. {exc}")

   
# Normal com formatação
# try:
#     with open(ROOT_PATH / "usuarios.csv", 'r', newline="", encoding="utf-8") as arquivo:
#         leitor = csv.reader(arquivo)
#         for idx,row in enumerate(leitor):
#             if idx == 0:
#                 continue
#             print(f"ID: {row[COLUNA_ID]}")
#             print(f"Nome: {row[COLUNA_NOME]}")
# except IOError as exc:
#     print(f"Erro ao abrir o arquivo. {exc}")

   
# Usando o DictReader
# try:
#     with open(ROOT_PATH / "usuarios.csv", newline="") as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             print(row["id"], row["nome"])
# except IOError as exc:
#     print(f"Erro ao abrir o arquivo. {exc}")
 
    
# Adaptando o DictReader para chamar pelo nome da coluna
try:
    with open(ROOT_PATH / "usuarios.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            #print(reader.fieldnames)
            print(f"ID: {row['id']}")
            print(f"Nome: {row['nome']}")
except IOError as exc:
    print(f"Erro ao abrir o arquivo. {exc}")