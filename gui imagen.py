from cProfile import label
from cgitb import text
from select import select
from tkinter import *
from tkinter import filedialog
from tkinter.font import BOLD
from xml.dom.minidom import ReadOnlySequentialNamedNodeMap
from PIL import Image
from PIL import ImageTk
import cv2
import imutils
import numpy as np

def detect_color():
    global image
    if selected.get() ==1:
        #rojo
        rangobajo1 = np.array([0,140,90], np.uint8)
        rangoalto1 = np.array([8,255,255], np.uint8)
        rangobajo2 = np.array([160,140,190], np.uint8)
        rangoalto2 = np.array([180,255,255], np.uint8)
    if selected.get() ==2:
        #amarillo
        rangobajo = np.array([10,98,0],np.uint8)
        rangoalto = np.array([25,255,255],np.uint8)
    if selected.get() ==3:
        #azul
        rangobajo = np.array([88,104,121],np.uint8)
        rangoalto = np.array([99,255,243],np.uint8)
    imagegray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    imagegray = cv2.cvtColor(imagegray, cv2.COLOR_GRAY2BGR)
    imageHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    if selected.get() == 1:
        #si es rojo...
    
        maskrojo1 = cv2.inRange(imageHSV, rangobajo1, rangoalto1)
        maskrojo2 = cv2.inRange(imageHSV, rangobajo2, rangoalto2)
        mask = cv2.add(maskrojo1, maskrojo2)
    else:
        mask = cv2.inRange(imageHSV, rangobajo, rangoalto)

    mask = cv2.medianBlur(mask, 7)
    color_detected = cv2.bitwise_and(image, image, mask=mask)

    #fondo en grises
    invmask = cv2.bitwise_not(mask)
    bggray = cv2.bitwise_and(imagegray, imagegray, mask=invmask)
    
    #suma de bggray y color_detected
    finalimage = cv2.add(bggray, color_detected)
    imagetoshowoutput = cv2.cvtColor(finalimage, cv2.COLOR_BGR2RGB)

    #que se vea la final en la gui
    im = Image.fromarray(imagetoshowoutput)
    img = ImageTk.PhotoImage(image=im)
    outimglabel.configure(image=img)
    outimglabel.image = img

    #texto de imagen de salida
    info3label = Label(root, text="imagen resultado", font="bold")
    info3label.grid(column=1, row=0, padx=5, pady=5)

def elegir_img():
    #especificar que tipos de arvhivos lee
    dir_img = filedialog.askopenfilename(filetypes=[("image",".jpg"),("image",".jpeg"),("image",".png")])

    if len(dir_img) > 0:
        global image
        #leer la imagen con open cv
        image = cv2.imread(dir_img)
        image = imutils.resize(image, height=380) #redimencionar imagen a 380 de alto

        #para ver la imagen chiquita
        img_para_nmostrar = imutils.resize(image, width=180)
        img_para_nmostrar = cv2.cvtColor(img_para_nmostrar, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(img_para_nmostrar)
        img = ImageTk.PhotoImage(image=im)


        inimagelabel.config(image=img)
        inimagelabel.image = img

        #label sobre la imagen chiquita
        info_label = Label(root, text="imagen de entrada")
        info_label.grid(column=0, row=1, padx=5, pady=5)


image = None

#crear ventana principal
root  = Tk()

#label para la imagen
inimagelabel = Label(root)
inimagelabel.grid(column=0, row=2)

#label para presentar la imagen de salida
outimglabel = Label(root)
outimglabel.grid(column=1, row=1, rowspan=6)

label_info2 = Label(root, text="que color le ponemos?", width=25)
label_info2.grid(column=0,row=3,padx=5,pady=5)

#botones redondos
selected = IntVar()
rad1 = Radiobutton(root, text="rojo",width=25,value=1,variable = selected, command=detect_color)
rad2 = Radiobutton(root, text="amarillo",width=25,value=2,variable = selected, command=detect_color)
rad3 = Radiobutton(root, text="azul",width=25,value=3,variable = selected, command=detect_color)
rad1.grid(column=0,row=4)
rad2.grid(column=0,row=5)
rad3.grid(column=0,row=6)

btn = Button(root, text="elegir imagen",width=25,command= elegir_img)
btn.grid(column=0, row=0, padx=5, pady=5)

root.mainloop()