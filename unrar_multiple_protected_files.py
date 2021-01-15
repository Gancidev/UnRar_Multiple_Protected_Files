#author:GanciDev

import os
from pathlib import Path
password = open("/path_to_the_file/password.txt", "r").readlines()
cont=0
for f in Path('.').glob('*.rar'):
    print(f)
    print(password[cont])
    comando="unrar x -p"+str(password[cont]).replace("\n","")+" "+str(f)
    print(comando)
    os.system(comando)
    cont=cont+1
