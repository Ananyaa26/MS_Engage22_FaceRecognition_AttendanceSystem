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
import os
import numpy as np


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition")

    # =========Background Image ===============
        
        img_behind=Image.open(r"Images\traindatabgimg.jpg")
        img_behind=img_behind.resize((1530,790),Image.ANTIALIAS)
        self.pimg_behind=ImageTk.PhotoImage(img_behind)

        be_img=Label(self.root,image=self.pimg_behind)
        be_img.place(x=0,y=0,width=1530,height=790)

    # =============Train Data BUtton ===========

        train_btn=Button(be_img,text="Train Data",command=self.train_classifier,cursor="hand2",font=("verdana",40,"bold","italic"),bg="black",fg="red")
        train_btn.place(x=400,y=300,width=500,height=80)



    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')  #Greyscale conversion
            imageNp=np.array(img, 'uint8')      #datatype

            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training the Images",imageNp)
            cv2.waitKey(1) == 13

        ids=np.array(ids)


# ========= SAVE AND TRAIN THE CLASSIFIER ==============

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()

        messagebox.showinfo("Result","The training of dataset is completed")




if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()
        