import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent
#print(ROOT_PATH.parent)

# Cria um novo diretório tilizando o caminho
#os.mkdir("/home/adduser/Manipulation_Archive) 

# Cria um novo diretório utilizando o caminho do Root path
#os.mkdir(ROOT_PATH / "New_Directory") 

#arquivo = open("/home/adduser/Manipulation_Archive/os_shutil_test.txt", "w")
#arquivo = open(ROOT_PATH / "move_test.txt", "w")
#arquivo = open(ROOT_PATH / "arquivo-utf-8", "w")
arquivo = open(ROOT_PATH / "Log.txt", "w")



#arquivo.close()

# Renomear o archivo
#os.rename(ROOT_PATH / "os_shutil_test.txt", ROOT_PATH / "os_shutil_Adjusted.txt")

# Remover um arquivo
#os.remove(ROOT_PATH / "remove_test.txt")

# Mover um arquivo
#shutil.move(ROOT_PATH / "move_test.txt", ROOT_PATH / "New_Directory" / "move_test.txt")