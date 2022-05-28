from ast import If
from cProfile import label
from ctypes import alignment
import imp
from multiprocessing.dummy import Value
from tabnanny import filename_only
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2


class Helpdesk:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition")



#Helpdesk image

        img00=Image.open(r"Images\helpdesk.jpg")
        img00=img00.resize((750,600),Image.ANTIALIAS)
        self.pimg00=ImageTk.PhotoImage(img00)

        bg_img=Label(self.root,image=self.pimg00)
        bg_img.place(x=20,y=20,width=750,height=600)

        #TITLE

        title_lbl=Label(self.root,text="Help Desk",font=("Hervetica",35,"bold","italic","underline"),bg="light yellow",fg="black")
        title_lbl.place(x=800,y=50,width=450,height=100)

        img0=Image.open(r"Images\Dev_Ananyaa.jpg.jpeg")
        img0=img0.resize((400,350),Image.ANTIALIAS)
        self.pimg0=ImageTk.PhotoImage(img0)

        dev_img=Label(self.root,image=self.pimg0)
        dev_img.place(x=850,y=151,width=400,height=350)

        title_lbl=Label(self.root,text="For any Query,E-Mail at:\n ananya.bansal7979@gmail.com",font=("Hervetica",25,"bold","italic"),bg="light yellow",fg="black")
        title_lbl.place(x=770,y=500,width=500,height=100)

if __name__ == "__main__":
    root=Tk()
    obj=Helpdesk(root)
    root.mainloop()