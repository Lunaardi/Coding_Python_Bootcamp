from pathlib import Path

ROOT_PATH = Path(__file__).parent

# Example 1
# try:
#     arquivo = open("my_archive.py")
# except FileNotFoundError as exc:
#     print("Arquivo não encontrado")
#     print(exc)

# # Example 2

# try:
#     arquivo = open(ROOT_PATH / "Novo_diretorio")
# except Exception as exc:
#     print(f"Não foi possivel abrir o arquivo {exc}")

# Example 3
# try:
#     arquivo = open("my_archive.py")
# except FileNotFoundError as exc:
#     print("Arquivo não encontrado")
#     print(exc)

# Example 4
try:
    arquivo = open("my_archive.py")
except FileNotFoundError as exc:
    print("Arquivo não encontrado")
    print(exc)
except IsADirectoryError as exc:
    print(f"Não foi possivel abrir o arquivo: {exc}")
except IOError as exc:
    print(f"Erro ao abrir o arquivo: {exc}")
except Exception as exc:
    print("Algum problema ocorreu ao tentar abrir um arquivo: {exc}")