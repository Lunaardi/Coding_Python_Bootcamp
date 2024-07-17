arquivo = open("/home/adduser/Manipulation_Archive/lorem.txt", "r")

#print(arquivo.read())
print(arquivo.readline())
#print(arquivo.readlines())

#exemplo quando queremos explorar um arquivo muito grande e contar o numero de caracteres
# while len(linha := arquivo.readline()):
#     print(linha)

# Outra maneira de usar o readline em primeira linha trazendo 1 caracter por linha
#for linha in arquivo.readline():
#    print(linha)

arquivo.close()