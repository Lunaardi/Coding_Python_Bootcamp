arquivo = open("/home/adduser/Manipulation_Archive/Write_test.txt", "w")

arquivo.write("Bitcoin é uma moeda descentralizada e não tem controlos governamentais, o que a torna uma boa opção para quem deseja ter controle sobre sua própria moeda.")   
arquivo.writelines(["\n","Python"])
arquivo.writelines(["\n", "Escrevendo", "um", "novo", "texto"])
arquivo.writelines(["\n", "Escrevendo", "\n", "um", "\n", "novo", "\n", "texto"])

arquivo.close()