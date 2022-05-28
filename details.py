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


class Details:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition")

        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_enrollmentno=StringVar()
        self.var_name=StringVar()
        self.var_gender=StringVar()
        self.var_phone=StringVar()
        self.var_emailid=StringVar()
        self.var_dob=StringVar()
        self.var_pic=StringVar()

#=============BackGround Image============

        img00=Image.open(r"Images\istockphoto-1268728034-170667a.jpg")
        img00=img00.resize((1530,790),Image.ANTIALIAS)
        self.pimg00=ImageTk.PhotoImage(img00)

        bg_img=Label(self.root,image=self.pimg00)
        bg_img.place(x=0,y=0,width=1530,height=790)

#================Title==================

        title_lbl=Label(bg_img,text="Personal Data",font=("Hervetica",35,"bold","italic","underline"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1300,height=100)

#===============MAIN FRAME =====================

        m_frame=Frame(bg_img,bd=4,bg="white")
        m_frame.place(x=13,y=120,width=1250,height=600)

    #=============LEFT BOX - Information ==================

        l_frame=LabelFrame(m_frame,bd=4,relief="groove",text="Information",font=("sans-serif",15,"italic"),fg="red",bg="white")
        l_frame.place(x=15,y=10,width=600,height=510)

        #=====Personal Information=======

        prsnl_frame=LabelFrame(l_frame,bd=4,relief="groove",text="Personal",font=("sans-serif",15,"bold"),fg="black",bg="white")
        prsnl_frame.place(x=10,y=10,width=570,height=290)

        #Image

        img_left=Image.open(r"Images\personal-info-data.jpg")
        img_left=img_left.resize((280,250),Image.ANTIALIAS)
        self.pimg_left=ImageTk.PhotoImage(img_left)

        l_img=Label(prsnl_frame,image=self.pimg_left)
        l_img.place(x=280,y=0,width=270,height=250)

        #Student ID

        id_lbl=Label(prsnl_frame,text="Student Id :",font=("sans-serif",11,"italic"),bg="white",fg="black")
        id_lbl.grid(row=0,column=0,padx=3,pady=1)
        id_entry =ttk.Entry(prsnl_frame,textvariable=self.var_std_id,width=13,font=("sans-serif",11))
        id_entry.grid(row=0,column=1,padx=3,pady=1)

        #Name

        n_lbl=Label(prsnl_frame,text="Name :",font=("sans-serif",11,"italic"),bg="white",fg="black")
        n_lbl.grid(row=1,column=0,padx=5)
        n_entry =ttk.Entry(prsnl_frame,textvariable=self.var_name,width=13,font=("sans-serif",11))
        n_entry.grid(row=1,column=1,padx=3,pady=1)

        #Enrollment Number

        id_lbl=Label(prsnl_frame,text="Enrollment No. :",font=("sans-serif",11,"italic"),bg="white",fg="black")
        id_lbl.grid(row=2,column=0,padx=5,pady=1)
        id_entry =ttk.Entry(prsnl_frame,textvariable=self.var_enrollmentno,width=13,font=("sans-serif",11))
        id_entry.grid(row=2,column=1,padx=3,pady=1)

        #Gender

        g_lbl=Label(prsnl_frame,text="Gender :",font=("sans-serif",11,"italic"),bg="white",fg="black")
        g_lbl.grid(row=3,column=0,padx=3,pady=1)

        g_comb=ttk.Combobox(prsnl_frame,textvariable=self.var_gender,font=("sans-serif",10,"italic"),width=12,state="readonly")
        g_comb["values"]=("Select Gender","Male","Female","Other")
        g_comb.current(0)
        g_comb.grid(row=3,column=1,padx=3,pady=1)

        #DOB

        dob_lbl=Label(prsnl_frame,text="Date of Birth :",font=("sans-serif",11,"italic"),bg="white",fg="black")
        dob_lbl.grid(row=4,column=0,padx=5)
        dob_entry =ttk.Entry(prsnl_frame,textvariable=self.var_dob,width=13,font=("sans-serif",11))
        dob_entry.grid(row=4,column=1,padx=3,pady=1)

        #Phone number

        phn_lbl=Label(prsnl_frame,text="Phone Number :",font=("sans-serif",11,"italic"),bg="white",fg="black")
        phn_lbl.grid(row=5,column=0,padx=5,pady=1)
        phn_entry =ttk.Entry(prsnl_frame,textvariable=self.var_phone,width=13,font=("sans-serif",11))
        phn_entry.grid(row=5,column=1,padx=3,pady=1)

        #Email Id

        e_lbl=Label(prsnl_frame,text="Email Id :",font=("sans-serif",11,"italic"),bg="white",fg="black")
        e_lbl.grid(row=6,column=0,padx=3,pady=1)
        e_entry =ttk.Entry(prsnl_frame,textvariable=self.var_emailid,width=13,font=("sans-serif",11))
        e_entry.grid(row=6,column=1,padx=3,pady=1)

        #Radio Buttons
        self.var_r1=StringVar()
        rbtn1=ttk.Radiobutton(prsnl_frame,variable=self.var_r1,text="Take Picture",value="Yes")
        rbtn1.grid(row=7,column=0,padx=1,pady=1)

        rbtn2=ttk.Radiobutton(prsnl_frame,variable=self.var_r1,text="No Picture",value="No")
        rbtn2.grid(row=7,column=1,padx=1,pady=1)

        # Pink buttons

        s_btn=Button(prsnl_frame,text="Save",command=self.add_data,font=("sans-serif",8,"bold"),bg="pink",fg="black",width=16)
        s_btn.grid(row=8,column=0,pady=1)

        r_btn=Button(prsnl_frame,text="Reset",command=self.reset_data,font=("sans-serif",8,"bold"),bg="pink",fg="black",width=16)
        r_btn.grid(row=8,column=1,pady=1)

        take_photo=Button(prsnl_frame,command=self.gen_dataset ,text="Take Photo",font=("sans-serif",8,"bold"),bg="pink",fg="black",width=16)
        take_photo.grid(row=9,column=0,pady=1)

        update_photo=Button(prsnl_frame,text="Update Photo",font=("sans-serif",8,"bold"),bg="pink",fg="black",width=16)
        update_photo.grid(row=9,column=1,pady=1)


        #=====Course Information=======

        course_frame=LabelFrame(l_frame,bd=4,relief="groove",text="Course",font=("sans-serif",15,"bold"),fg="black",bg="white")
        course_frame.place(x=10,y=300,width=570,height=170)

        #Department name

        dep_lbl=Label(course_frame,text="Department Name",font=("sans-serif",15,"italic"),bg="white",fg="black")
        dep_lbl.grid(row=0,column=0,padx=7)

        dep_comb=ttk.Combobox(course_frame,textvariable=self.var_dep,font=("sans-serif",12,"italic"),width=25,state="readonly")
        dep_comb["values"]=("Select Department","Commerce","Arts","Science","Law","Medical","Music","Dance","Management","Technology")
        dep_comb.current(0)
        dep_comb.grid(row=1,column=0,pady=1,padx=7)

        #Course Name

        c_lbl=Label(course_frame,text="Course Name",font=("sans-serif",15,"italic"),bg="white",fg="black")
        c_lbl.grid(row=3,column=0,padx=7)

        c_comb=ttk.Combobox(course_frame,textvariable=self.var_course,font=("sans-serif",12,"italic"),width=25,state="readonly")
        c_comb["values"]=("Select Course","B.Tech","B.Sc","MBBS","PhD","Diploma","Hons","M.Tech","BBA","MBA")
        c_comb.current(0)
        c_comb.grid(row=4,column=0,pady=1,padx=7)

        #Current Year 

        y_lbl=Label(course_frame,text="Current Year",font=("sans-serif",15,"italic"),bg="white",fg="black")
        y_lbl.grid(row=0,column=1,padx=28)

        y_comb=ttk.Combobox(course_frame,textvariable=self.var_year,font=("sans-serif",12,"italic"),width=25,state="readonly")
        y_comb["values"]=("Select Year","First","Second","Third","Fourth","Fifth")
        y_comb.current(0)
        y_comb.grid(row=1,column=1,pady=1,padx=28)

        #Current Sem

        s_lbl=Label(course_frame,text="Current Semester",font=("sans-serif",15,"italic"),bg="white",fg="black")
        s_lbl.grid(row=3,column=1,padx=28)

        s_comb=ttk.Combobox(course_frame,textvariable=self.var_semester,font=("sans-serif",12,"italic"),width=25,state="readonly")
        s_comb["values"]=("Select Semester","1st","2nd","3rd","4th","5th","6th","7th","8th")
        s_comb.current(0)
        s_comb.grid(row=4,column=1,pady=1,padx=28)

    #============RIGHT BOX- Display of details===========

                                               

        r_frame=LabelFrame(m_frame,bd=4,relief="groove",text="Details",font=("sans-serif",15,"italic"),fg="red",bg="white")
        r_frame.place(x=630,y=10,width=600,height=510)

        img_right=Image.open(r"Images\data-icon.png")
        img_right=img_right.resize((250,200),Image.ANTIALIAS)
        self.pimg_right=ImageTk.PhotoImage(img_right)

        r_img=Label(r_frame,image=self.pimg_right)
        r_img.place(x=3,y=0,width=250,height=200)


        #==========SEARCH FRAME===============

        search_frame=LabelFrame(r_frame,bd=4,relief="groove",text="Search Details",font=("sans-serif",15,"bold"),fg="black",bg="white")
        search_frame.place(x=260,y=0,width=325,height=200)

        search_lbl=Label(search_frame,text="Search by: ",font=("sans-serif",15,"italic"),bg="light yellow",fg="black")
        search_lbl.grid(row=0,column=0,padx=3,pady=4)

        self.var_combosearch=StringVar()
        search_comb=ttk.Combobox(search_frame,textvariable=self.var_combosearch,font=("sans-serif",12,"italic"),width=30,state="readonly")
        search_comb["values"]=("Select Category","Department","Course","Current Year","Current Semester","Name","Enrollment No.","Gender","Student ID","Photo Status")
        search_comb.current(0)
        search_comb.grid(row=1,column=0,pady=4,padx=5)

        self.var_search=StringVar()
        search_entry =ttk.Entry(search_frame,textvariable=self.var_search,width=25,font=("sans-serif",12))
        search_entry.grid(row=2,column=0,padx=2,pady=4)

        search_btn=Button(search_frame,command=self.search_data,text="Search 🔍",font=("sans-serif",10,"bold"),bg="pink",fg="black",width=33)
        search_btn.grid(row=3,column=0,pady=4)

        showall_btn=Button(search_frame,command=self.f_data,text="Show All",font=("sans-serif",10,"bold"),bg="pink",fg="black",width=33)
        showall_btn.grid(row=4,column=0,pady=4)


        #============ TABLE FRAME==============


        d_frame=LabelFrame(r_frame,bd=4,relief="groove",text="Display Details",font=("sans-serif",15,"bold"),fg="black",bg="white")
        d_frame.place(x=10,y=200,width=570,height=270)

        #Scrollbar

        scroll_x=ttk.Scrollbar(d_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(d_frame,orient=VERTICAL)

        self.d_table=ttk.Treeview(d_frame,column=("dep","Course","Year","Semester","ID","Enrollment","Name","Gender","Phone","Email","DOB","Photo"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set )

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.d_table.xview)
        scroll_y.config(command=self.d_table.yview)

        # Table Headings

        self.d_table.heading("dep",text="Department")
        self.d_table.heading("Course",text="Course")
        self.d_table.heading("Year",text="Current Year")
        self.d_table.heading("Semester",text="Current Semester")
        self.d_table.heading("ID",text="Student ID")
        self.d_table.heading("Enrollment",text="Enrollment No.")
        self.d_table.heading("Name",text="Name")
        self.d_table.heading("Gender",text="Gender")
        self.d_table.heading("Phone",text="Phone No.")
        self.d_table.heading("Email",text="Email ID")
        self.d_table.heading("DOB",text="DOB")
        self.d_table.heading("Photo",text="Photo Status")
        self.d_table['show']="headings"

        self.d_table.column("dep",width=100)
        self.d_table.column("Course",width=50)
        self.d_table.column("Year",width=100)
        self.d_table.column("Semester",width=100)
        self.d_table.column("ID",width=80)
        self.d_table.column("Enrollment",width=150)
        self.d_table.column("Name",width=100)
        self.d_table.column("Gender",width=50)
        self.d_table.column("Phone",width=100)
        self.d_table.column("Email",width=120)
        self.d_table.column("DOB",width=100)
        self.d_table.column("Photo",width=150)

        self.d_table.pack(fill=BOTH,expand=1)
        self.d_table.bind("<ButtonRelease>",self.get_cursor)
        self.f_data()


#===========Function Declaration=============

    #Error show if the fields are Empty

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","Fill the Empty Fields",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Sanskrit@12",database="face_recognizer")
                my_cursor=conn.cursor()
                #Execute the query
                my_cursor.execute("insert into details values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                                            self.var_dep.get(),
                                                                                            self.var_course.get(),
                                                                                            self.var_year.get(),
                                                                                            self.var_semester.get(),
                                                                                            self.var_std_id.get(),
                                                                                            self.var_enrollmentno.get(),
                                                                                            self.var_name.get(),
                                                                                            self.var_gender.get(),
                                                                                            self.var_phone.get(),
                                                                                            self.var_emailid.get(),
                                                                                            self.var_dob.get(),
                                                                                            self.var_r1.get()

                                                                                                        ))
                conn.commit()
                self.f_data()
                conn.close()
                messagebox.showinfo("Success","Details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

                
#===================Display the data to the right frame on clicking save button ==================

    def f_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Sanskrit@12",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
        data=my_cursor.fetchall()

        if len(data) != 0:
            self.d_table.delete(*self.d_table.get_children())
            for i in data:
                self.d_table.insert("",END,values=i)
            conn.commit()
        conn.close()

#=================Displaying of data in the left frame on selection of table rows==============

    def get_cursor(self,event=""):

        cursor_focus=self.d_table.focus()
        content=self.d_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_enrollmentno.set(data[5])
        self.var_name.set(data[6])
        self.var_gender.set(data[7])
        self.var_phone.set(data[8])
        self.var_emailid.set(data[9])
        self.var_dob.set(data[10])
        self.var_r1.set(data[11])

#======================Reset button==========================

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_enrollmentno.set("")
        self.var_name.set("")
        self.var_gender.set("Select Gender")
        self.var_phone.set(" ")
        self.var_emailid.set(" ")
        self.var_dob.set(" ")
        self.var_r1.set("")


# ====================Search button ==========================

    def search_data(self):
        if self.var_combosearch.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","Please select option")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Sanskrit@12",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from details where "+str(self.var_combosearch.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                data=my_cursor.fetchall()
                if len(data) !=0:
                    self.d_table.delete(*self.d_table.get_children())
                    for i in data:
                        self.d_table.insert("",END,values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                    messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

# =================Generate Photo Sample=====================


    def gen_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","Fill the Empty Fields",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Sanskrit@12",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from details")
                my_result=my_cursor.fetchall()

                id=0
                for x in my_result:
                    id+=1
                my_cursor.execute("update details set dep=%s,Course=%s,Year=%s,Semester=%s,Enrollment=%s,Name=%s,Gender=%s,Phone=%s,Email=%s,DOB=%s,Photo=%s where ID =%s",(
                                                                                            
                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                            self.var_semester.get(),
                                                                                                                                                                            self.var_enrollmentno.get(),
                                                                                                                                                                            self.var_name.get(),
                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                            self.var_emailid.get(),
                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                            self.var_r1.get(),
                                                                                                                                                                            self.var_std_id.get()==id+1
                                                                                                                                                                            
                                                                                                                                                                           ))
                                    
                conn.commit()
                self.f_data()
                self.reset_data()
                conn.close()

   
 # ============== Load frontal face Haarscascade default code from OpenCV ==================

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)  #Scaling Factor and minimum neighbour

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:

                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_SIMPLEX,3,(0,255,0),2)
                        cv2.imshow("Capturing Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:          #Condition to Capture 100 images
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generation of data completed Successfully")
            
            except Exception as es:
                 messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
      



if __name__ == "__main__":
    root=Tk()
    obj=Details(root)
    root.mainloop()
        
