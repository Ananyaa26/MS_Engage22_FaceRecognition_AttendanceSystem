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
from main import Face_Recognition

class Login_Window:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition")

        bg_img=Image.open(r"Images\background-image-for-login-page.jpg")
        bg_img=bg_img.resize((1350,770),Image.ANTIALIAS)
        self.pbg_img=ImageTk.PhotoImage(bg_img)

        bg_img=Label(self.root,image=self.pbg_img)
        bg_img.place(x=0,y=0,width=1350,height=770)

        login_frame=Frame(bg_img,bd=4,bg="white")
        login_frame.place(x=470,y=150,width=340,height=450)

#===========USER IMAGE===========  
        user_img=Image.open(r"Images\user.png")
        user_img=user_img.resize((80,80),Image.ANTIALIAS)
        self.puser_img=ImageTk.PhotoImage(user_img)

        user_img=Label(self.root,image=self.puser_img)
        user_img.place(x=600,y=152,width=80,height=80)

        n_lbl=Label(login_frame,text="Get Started!",font=("sans-serif",19,"bold"),bg="White",fg="dark blue")
        n_lbl.place(x=93,y=88)

#============Username==========

        username_lbl=Label(login_frame,text="Username",font=("sans-serif",14,"italic","bold"),bg="White",fg="black")
        username_lbl.place(x=15,y=140)

        self.user_entry =ttk.Entry(login_frame,width=13,font=("sans-serif",11,"bold"))
        self.user_entry.place(x=15,y=170,width=300,height=35)

#===========Password========
        Password_lbl=Label(login_frame,text="Password",font=("sans-serif",14,"italic","bold"),bg="White",fg="black")
        Password_lbl.place(x=15,y=220)

        self.password_entry =ttk.Entry(login_frame,width=13,font=("sans-serif",11,"bold"))
        self.password_entry.place(x=15,y=250,width=300,height=35)

#=========LOGIN BUTTON===========

        login_btn=Button(login_frame,text="LOGIN",command=self.main_page,font=("sans-serif",14,"bold"),bg="dark blue",fg="white",cursor="hand2")
        login_btn.place(x=100,y=290,width=120,height=50)

#===========Register Button==========

        register_btn=Button(login_frame,text="New User Register",font=("sans-serif",8,"italic","bold"),bg="dark blue",fg="white",cursor="hand2")
        register_btn.place(x=20,y=350,width=110,height=30)

        forgot_btn=Button(login_frame,text="Forgot Password?",font=("sans-serif",8,"italic","bold"),bg="dark blue",fg="white",cursor="hand2")
        forgot_btn.place(x=20,y=390,width=110,height=30)

#=====Login Function===========

    def login(self):
        if self.user_entry.get()=="" or self.password_entry.get()=="":
            messagebox.showerror("Error","Fill the Empty Fields",parent=self.root)
        elif self.user_entry.get()=="Ananyaa" and self.password_entry.get()=="Test@12":
            messagebox.showinfo("Success","Welcome to Attendance Tool via Face Recognition ",parent=self.root)
        else:
            messagebox.showerror("Error","Invalid Username and Password",parent=self.root)


    def main_page(self):
        self.new_window=Toplevel(self.root)
        self.p_d=Face_Recognition(self.new_window)

if __name__ == "__main__":
    
    root=Tk()
    obj=Login_Window(root)
    root.mainloop()
        
