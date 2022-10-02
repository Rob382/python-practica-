#watchdog move & copy
import os
import shutil
from pathlib import Path
os.chdir('c:/Users/miyav/videos/prueba-wdog')

if not os.path.exists("otro_folder"):
    os.mkdir("otro_folder")

for file in os.listdir():
    if file == 'otro_folder':
        continue
    print(file)
    #shutil.move(file, 'otro_folder')   #mueve el archivo file al folder otro_folder
    # shutil.copy(file, 'otro_folder')    #copia el archivo con fecha de creacion del momento que lo hizo
    shutil.copy2(file, 'otro_folder')    #copia el archivo con fecha de creacion original (metadata)