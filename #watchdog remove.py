#watchdog remove
import os
import shutil
from pathlib import Path
os.chdir('c:/Users/miyav/videos/prueba-wdog')

# os.remove("filename")       #elimina el archivo
# os.rmdir("otro_folder")     #elimina el folder si esta vacio
shutil.rmtree("otro_folder")    #elimina el folder y lo que tenga (recursivo)