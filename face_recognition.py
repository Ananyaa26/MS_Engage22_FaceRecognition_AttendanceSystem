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
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np


class Face_Detector:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition")

        facescan=Image.open(r"Images\facial-recognition-software-image.jpg")
        facescan=facescan.resize((1350,660),Image.ANTIALIAS)
        self.pfacescan=ImageTk.PhotoImage(facescan)

        facescan_lbl=Label(self.root,image=self.pfacescan)
        facescan_lbl.place(x=0,y=0,width=1350,height=660)

        #BUTTON
        detect_btn=Button(facescan_lbl,command=self.face_recog,text="DETECT YOUR FACE",cursor="hand2",font=("Helvetica",18,"bold"),bg="red",fg="white")
        detect_btn.place(x=470,y=50,width=400,height=55)

# ============ attendance ===========

    def mark_attendance(self,i,g,n,d):
        with open ("attendancerecord.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (g not in name_list) and (n not in name_list) and (d not in name_list) ) :
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{g},{n},{d},{dtString},{d1},Present")
            

# ======================Face detect================

    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="Sanskrit@12",database="face_recognizer")
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from details where ID ="+str(id))
                n=my_cursor=conn.fetchone()
                n="+".join(n)

                my_cursor.execute("select dep from details where ID ="+str(id))
                d=my_cursor=conn.fetchone()
                d="+".join(d)

                my_cursor.execute("select Gender from details where ID ="+str(id))
                g=my_cursor=conn.fetchone()
                g="+".join(g)

                my_cursor.execute("select ID from details where ID ="+str(id))
                i=my_cursor=conn.fetchone()
                i="+".join(i)
                


                if confidence>79:
                    cv2.putText(img,f"ID :{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Gender:{g}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,g,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord[x,y,w,h]

            return coord

        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while (video_cap.isOpened()):

            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Face Recognizer",img)

            if cv2.waitKey(30) & 0xFF == ord('q'):
                break
        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root=Tk()
    obj=Face_Detector(root)
    root.mainloop()