from cProfile import label
from ctypes import alignment
import imp
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from details import Details
import os
from train import Train
from face_recognition import Face_Detector
from attendance import Attendance
from helpdesk import Helpdesk

class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition")

    #BackGround Image

        img00=Image.open(r"Images\gradient-soft-cloudy.webp")
        img00=img00.resize((1530,790),Image.ANTIALIAS)
        self.pimg00=ImageTk.PhotoImage(img00)

        bg_img=Label(self.root,image=self.pimg00)
        bg_img.place(x=0,y=0,width=1530,height=790)


    #Details 

        img0=Image.open(r"Images\download (1).png")
        img0=img0.resize((200,180),Image.ANTIALIAS)
        self.pimg0=ImageTk.PhotoImage(img0)

        b0=Button(bg_img,image=self.pimg0,command=self.personal_data,cursor="hand2")
        b0.place(x=200,y=250,width=200,height=180)

        b0_0=Button(bg_img,text="Details",command=self.personal_data,font=("Verdana",15,"bold"),bg="pink",fg="black",cursor="hand2")
        b0_0.place(x=200,y=430,width=200,height=30)

    #Face Recognition 

        img1=Image.open(r"Images\images.png")
        img1=img1.resize((200,180),Image.ANTIALIAS)
        self.pimg1=ImageTk.PhotoImage(img1)


        b1=Button(bg_img,image=self.pimg1,cursor="hand2",command=self.face_data)
        b1.place(x=525,y=250,width=200,height=180)

        b1_1=Button(bg_img,text="Face Recognition",cursor="hand2",command=self.face_data,font=("Verdana",15,"bold"),bg="pink",fg="black")
        b1_1.place(x=525,y=430,width=200,height=30)

    #Attendance 


        img2=Image.open(r"Images\2620267.png")
        img2=img2.resize((200,180),Image.ANTIALIAS)
        self.pimg2=ImageTk.PhotoImage(img2)


        b2=Button(bg_img,image=self.pimg2,command=self.attendance_data,cursor="hand2")
        b2.place(x=850,y=250,width=200,height=180)

        b2_2=Button(bg_img,text="Attendance",command=self.attendance_data,font=("Verdana",15,"bold"),bg="pink",fg="black",cursor="hand2")
        b2_2.place(x=850,y=430,width=200,height=30)

    # Train Data

        img3=Image.open(r"Images\download.png")
        img3=img3.resize((60,60),Image.ANTIALIAS)
        self.pimg3=ImageTk.PhotoImage(img3)

        b3=Button(bg_img,command=self.train_data,image=self.pimg3,cursor="hand2")
        b3.place(x=950,y=580,width=60,height=60)


    # Photos

        img4=Image.open(r"Images\photos.png")
        img4=img4.resize((60,60),Image.ANTIALIAS)
        self.pimg4=ImageTk.PhotoImage(img4)


        b4=Button(bg_img,command=self.open_img,image=self.pimg4,cursor="hand2")
        b4.place(x=1050,y=580,width=60,height=60)

       

    # Helpdesk
        
        img5=Image.open(r"Images\images (2).png")
        img5=img5.resize((60,60),Image.ANTIALIAS)
        self.pimg5=ImageTk.PhotoImage(img5)


        b5=Button(bg_img,image=self.pimg5,command=self.helpdesk_data,cursor="hand2")
        b5.place(x=1150,y=580,width=60,height=60)


   #Title

        title_lbl=Label(bg_img,text="Tracking Attendance via Face Recognition Tool",font=("Verdana",30,"bold","italic"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1350,height=80)

    



#=========================Functions=======================

    def personal_data(self):
        self.new_window=Toplevel(self.root)
        self.p_d=Details(self.new_window)

    def open_img(self):
        os.startfile("data")

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.p_d=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.p_d=Face_Detector(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.p_d=Attendance(self.new_window)

    def helpdesk_data(self):
        self.new_window=Toplevel(self.root)
        self.p_d=Helpdesk(self.new_window)




if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()
        