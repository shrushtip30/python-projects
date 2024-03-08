from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class reportClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result management system")
        self.root.geometry("1200x480+80+170")
        self.root.configure(bg="white")
        self.root.focus_force()
        #title
        title=Label(self.root,text="View Student Results", font=("goudy old style",20,"bold"),bg="orange",fg="black").place(x=10,y=15,width=1180,height=50)
        #search
        self.var_search=StringVar()
        lbl_student=Label(self.root,text="Search by Roll no", font=("goudy old style",20,"bold"),bg="white").place(x=300,y=100)
        txt_student=Entry(self.root,textvariable=self.var_search,font=("goudy old style",20),bg="light yellow",fg="black").place(x=520,y=100,width=150)
        btn_search=Button(self.root,text="Search",font=("arial",15,"bold"),bg="navy blue",fg="white",cursor="hand2").place(x=680,y=100,width=110,height=40)
        btn_clear=Button(self.root,text="Clear",font=("arial",15,"bold"),bg="green",fg="white",cursor="hand2").place(x=800,y=100,width=110,height=40)

        lbl_roll=Label(self.root,text="Roll No.", font=("goudy old style",20,"bold"),bg="white",bd=2,relief=GROOVE).place(x=150,y=230,width=150,height=50)
        lbl_name=Label(self.root,text="Name", font=("goudy old style",20,"bold"),bg="white",bd=2,relief=GROOVE).place(x=300,y=230,width=150,height=50)
        lbl_course=Label(self.root,text="Course", font=("goudy old style",20,"bold"),bg="white",bd=2,relief=GROOVE).place(x=450,y=230,width=150,height=50)
        lbl_marks_ob=Label(self.root,text="Marks Obtained", font=("goudy old style",20,"bold"),bg="white",bd=2,relief=GROOVE).place(x=600,y=230,width=190,height=50)
        lbl_full=Label(self.root,text="Total Marks", font=("goudy old style",20,"bold"),bg="white",bd=2,relief=GROOVE).place(x=790,y=230,width=150,height=50)
        
        
        self.roll=Label(self.root,font=("goudy old style",20,"bold"),bg="white",bd=2,relief=GROOVE)
        self.roll.place(x=150,y=230,width=150,height=50)
        self.name=Label(self.root,font=("goudy old style",20,"bold"),bg="white",bd=2,relief=GROOVE).place(x=300,y=230,width=150,height=50)
        self.course=Label(self.root,font=("goudy old style",20,"bold"),bg="white",bd=2,relief=GROOVE).place(x=450,y=230,width=150,height=50)
        self.marks_ob=Label(self.root,font=("goudy old style",20,"bold"),bg="white",bd=2,relief=GROOVE).place(x=600,y=230,width=190,height=50)
        self.full=Label(self.root,font=("goudy old style",20,"bold"),bg="white",bd=2,relief=GROOVE).place(x=790,y=230,width=150,height=50)
        

if __name__=="__main__":
    root=Tk()
    obj=reportClass(root)
    root.mainloop()