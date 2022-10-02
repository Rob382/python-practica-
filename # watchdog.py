# watchdog rename
import os
print(os.getcwd())
os.chdir('c:/Users/miyav/videos/prueba-wdog')
print(os.getcwd())
for file in os.listdir():
    name, ext = os.path.splitext(file)
    #print(name, ext)
    splitname = name.split('-')
    print(splitname)
    #print(len(splitname))
    newname = f"{splitname[3]}-{splitname[4]}-{splitname[5]}_{splitname[2]}-{splitname[1]}-{splitname[0]}{ext}"
    print(newname)
    os.rename(file, newname)

