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
import os
import cv2
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition")

#   ============= Variables===========

        self.var_attend_id=StringVar()
        self.var_name=StringVar()
        self.var_enrollno=StringVar()
        self.var_gend=StringVar()
        self.var_date=StringVar()
        self.var_time=StringVar()
        self.var_attend_status=StringVar()

    #BackGround Image

        img00=Image.open(r"Images\istockphoto-1268728034-170667a.jpg")
        img00=img00.resize((1530,790),Image.ANTIALIAS)
        self.pimg00=ImageTk.PhotoImage(img00)

        bg_img=Label(self.root,image=self.pimg00)
        bg_img.place(x=0,y=0,width=1530,height=790)

    #Title

        title_lbl=Label(bg_img,text="Attendance Record",font=("Hervetica",35,"bold","italic","underline"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1300,height=100)

#Frame

        m_frame=Frame(bg_img,bd=4,bg="white")
        m_frame.place(x=13,y=120,width=1250,height=600)

#LEFT BOX 

                                 #Student information

        l_frame=LabelFrame(m_frame,bd=4,relief="groove",text="Attendance Information",font=("sans-serif",15,"italic"),fg="red",bg="white")
        l_frame.place(x=15,y=10,width=600,height=510)

        
        img_left=Image.open(r"Images\attendance header.jpg")
        img_left=img_left.resize((580,180),Image.ANTIALIAS)
        self.pimg_left=ImageTk.PhotoImage(img_left)

        l_img=Label(l_frame,image=self.pimg_left)
        l_img.place(x=0,y=8,width=580,height=180)

        #Second frame in left box

        l_inside_frame=LabelFrame(l_frame,bd=4,relief="groove",text="==================================================================",font=("sans-serif",15,"italic"),fg="red",bg="white")
        l_inside_frame.place(x=5,y=193,width=580,height=250)

#attendance id

        attendance_id=Label(l_inside_frame,text="Attendance_Id:",font=("sans-serif",15,"italic"),bg="brown",fg="white")
        attendance_id.grid(row=0,column=0,padx=5,pady=2)
        attendance_id_entry =ttk.Entry(l_inside_frame,textvariable=self.var_attend_id,width=20,font=("sans-serif",15))
        attendance_id_entry.grid(row=0,column=1,padx=5,pady=2)

#name
        n_lbl=Label(l_inside_frame,text="Name :",font=("sans-serif",15,"italic"),bg="brown",fg="white")
        n_lbl.grid(row=1,column=0,padx=5)
        n_attend =ttk.Entry(l_inside_frame,textvariable=self.var_name,width=20,font=("sans-serif",15))
        n_attend.grid(row=1,column=1,padx=3,pady=2)

#enroll no.
        
        id_lbl=Label(l_inside_frame,text="Enrollment No.:",font=("sans-serif",15,"italic"),bg="brown",fg="white")
        id_lbl.grid(row=2,column=0,padx=5,pady=2)
        id_attend =ttk.Entry(l_inside_frame,width=20,textvariable=self.var_enrollno,font=("sans-serif",15))
        id_attend.grid(row=2,column=1,padx=3,pady=2)

#date
        date_lbl=Label(l_inside_frame,text="Date :",font=("sans-serif",15,"italic"),bg="brown",fg="white")
        date_lbl.grid(row=3,column=0,padx=5)
        date_attend =ttk.Entry(l_inside_frame,textvariable=self.var_date,width=20,font=("sans-serif",15))
        date_attend.grid(row=3,column=1,padx=3,pady=2)
#time

        time_lbl=Label(l_inside_frame,text="Time :",font=("sans-serif",15,"italic"),bg="brown",fg="white")
        time_lbl.grid(row=4,column=0,padx=5)
        time_attend =ttk.Entry(l_inside_frame,textvariable=self.var_time,width=20,font=("sans-serif",15))
        time_attend.grid(row=4,column=1,padx=3,pady=2)

#attendance       

        attendance_lbl=Label(l_inside_frame,text="Attendance Status :",font=("sans-serif",15,"italic"),bg="brown",fg="white")
        attendance_lbl.grid(row=5,column=0,padx=3,pady=2)

        self.attend_status=ttk.Combobox(l_inside_frame,textvariable=self.var_attend_status,font=("sans-serif",12,"italic"),width=20,state="readonly")
        self.attend_status["values"]=("Status","Present","Absent")
        self.attend_status.current(0)
        self.attend_status.grid(row=5,column=1,padx=3,pady=2)

#buttons 

        imp_btn=Button(l_frame,text="Import",command=self.importCSV,font=("sans-serif",10,"bold"),bg="pink",fg="black",width=20)
        imp_btn.place(x=5,y=440,width=130,height=40)        

        exp_btn=Button(l_frame,text="Export",command=self.exportCSV,font=("sans-serif",10,"bold"),bg="pink",fg="black",width=20)
        exp_btn.place(x=136,y=440,width=130,height=40)

        r_btn=Button(l_frame,text="Reset",command=self.reset_data,font=("sans-serif",10,"bold"),bg="pink",fg="black",width=20)
        r_btn.place(x=267,y=440,width=130,height=40)

        update_btn=Button(l_frame,text="Update",font=("sans-serif",10,"bold"),bg="pink",fg="black",width=20)
        update_btn.place(x=398,y=440,width=130,height=40)


#RIGHT BOX
        #Display of details

        r_frame=LabelFrame(m_frame,bd=4,relief="groove",text="Attendance Record data",font=("sans-serif",15,"italic"),fg="red",bg="white")
        r_frame.place(x=630,y=10,width=600,height=510)

        table_frame=LabelFrame(r_frame,bd=4,relief="groove",text="Record of Attendance in Tabular Form",font=("sans-serif",12,"bold"),fg="black",bg="white")
        table_frame.place(x=5,y=5,width=580,height=470)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.attendancereporttable=ttk.Treeview(table_frame,column=("id","Name","Enrollment No.","Gender","Date","Time","Attendance Status"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set )

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.attendancereporttable.xview)
        scroll_y.config(command=self.attendancereporttable.yview)

        self.attendancereporttable.heading("id",text="Attendance Id")
        self.attendancereporttable.heading("Name",text="Name")
        self.attendancereporttable.heading("Enrollment No.",text="Enrollment No.")
        self.attendancereporttable.heading("Gender",text="Gender")
        self.attendancereporttable.heading("Date",text="Date")
        self.attendancereporttable.heading("Time",text="Time")
        self.attendancereporttable.heading("Attendance Status",text="Attendance Status")

        self.attendancereporttable['show']="headings"

        self.attendancereporttable.column("id",width=100)
        self.attendancereporttable.column("Name",width=100)
        self.attendancereporttable.column("Enrollment No.",width=120)
        self.attendancereporttable.column("Gender",width=70)
        self.attendancereporttable.column("Date",width=100)
        self.attendancereporttable.column("Time",width=100)
        self.attendancereporttable.column("Attendance Status",width=100)


        self.attendancereporttable.pack(fill=BOTH,expand=1)
        self.attendancereporttable.bind("<ButtonRelease>",self.get_cursor)

#=============================Function=================================
    def fetchData(self,rows):
        self.attendancereporttable.delete(*self.attendancereporttable.get_children())
        for i in rows:
            self.attendancereporttable.insert("",END,values=i)

#============IMPORT CSV FILE TO ATTENDANCE TABLE=============

    def importCSV(self):
        global mydata
        mydata.clear()

        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csv_read=csv.reader(myfile,delimiter=",")
            for i in csv_read:
                mydata.append(i)
            self.fetchData(mydata)

#============EXPORT CSV FILE FROM ATTENDANCE TABLE ==============

    def exportCSV(self):
            try:
                if len(mydata)<1:
                        messagebox.showerror("No Data","No Data is Found",parent=self.root)
                        return False
                fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
                with open(fln,mod="w",newline="") as myfile:
                        exp_write=csv.writer(myfile,delimiter=",")
                        for i in mydata:
                                exp_write.writerow(i)
                        messagebox.showinfo("Data Export","Data has been exported to "+os.path.basename(fln)+" Successfully!")
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

# ===========SHOW THE DATA FROM RIGHT FRAME TO LEFT SPACES=============

    def get_cursor(self,eve=""):
        cursor_row=self.attendancereporttable.focus()
        content=self.attendancereporttable.item(cursor_row)
        rows=content['values']

        self.var_attend_id.set(rows[0])
        self.var_name.set(rows[1])
        self.var_enrollno.set(rows[2])
        self.var_gend.set(rows[3])
        self.var_date.set(rows[4])
        self.var_time.set(rows[5])
        self.var_attend_status.set(rows[6])

# ====================RESET BUTTON FUNCTION==================
      
    def reset_data(self):
        self.var_attend_id.set("")
        self.var_name.set("")
        self.var_enrollno.set("")
        self.var_gend.set("")
        self.var_date.set("")
        self.var_time.set("")
        self.var_attend_status.set("")

if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()
