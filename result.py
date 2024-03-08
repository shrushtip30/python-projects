from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class resultClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result management system")
        self.root.geometry("1200x480+80+170")
        self.root.configure(bg="white")
        self.root.focus_force()
        #title
        title=Label(self.root,text="Add Student Results", font=("goudy old style",20,"bold"),bg="orange",fg="black").place(x=10,y=15,width=1180,height=50)
        
        #variables
        self.var_roll=StringVar()
        self.var_student=StringVar()
        self.var_name=StringVar()
        self.var_course=StringVar()
        self.var_marks_ob=StringVar()
        self.var_full_marks=StringVar()
        
        
        #widgets
        lbl_student=Label(self.root,text="Select Student", font=("goudy old style",20,"bold"),bg="white").place(x=10,y=70)
        lbl_name=Label(self.root,text="Name", font=("goudy old style",20,"bold"),bg="white").place(x=10,y=120)
        lbl_course=Label(self.root,text="Course", font=("goudy old style",20,"bold"),bg="white").place(x=10,y=170)
        lbl_marks_ob=Label(self.root,text="Marks Obtained", font=("goudy old style",20,"bold"),bg="white").place(x=10,y=220)
        lbl_full_marks=Label(self.root,text="Full Marks", font=("goudy old style",20,"bold"),bg="white").place(x=10,y=270)
        self.roll_list=[]
        self.fetch_roll()
        self.txt_student=ttk.Combobox(self.root,textvariable=self.var_roll,values=self.roll_list,font=("goudy old style",20,"bold"),state='readonly',justify=CENTER)
        self.txt_student.place(x=180,y=70,width=200)
        self.txt_student.set("Select")
        self.btn_add=Button(self.root,text="Search",font=("arial",15,"bold"),bg="navy blue",fg="white",cursor="hand2",command=self.search).place(x=400,y=70,width=110,height=40)
        #Entry Fields
        
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",20,"bold"),bg="light yellow",state='readonly').place(x=180,y=130)
        txt_course=Entry(self.root,textvariable=self.var_course,font=("goudy old style",20,"bold"),bg="light yellow",state='readonly').place(x=180,y=180)
        self.txt_marks_ob=Text(self.root,font=("goudy old style",20,"bold"),bg="light yellow").place(x=200,y=230,width=270,height=35)
        self.txt_full_marks=Text(self.root,font=("goudy old style",20,"bold"),bg="light yellow").place(x=200,y=280,width=270,height=35)

        #buttons
        self.btn_add=Button(self.root,text="Submit",font=("arial",15,"bold"),bg="light green",fg="black",cursor="hand2",command=self.add).place(x=80,y=400,width=110,height=40)
        self.btn_clear=Button(self.root,text="Clear",font=("arial",15,"bold"),bg="gray",fg="black",cursor="hand2",command=self.clear).place(x=210,y=400,width=110,height=40)

        #functions
    def fetch_roll(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
                
            cur.execute("select roll from student")
            rows=cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.roll_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def search(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            
            cur.execute(f"select name,course from student where roll=?",(self.var_roll.get(),))
            row=cur.fetchone()
            if row!=None:
                self.var_name.set(row[0])
                self.var_course.set(row[1])
                
            else:
                messagebox.showerror("Error","No record Found",parent=self.root)
            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def add(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","please first search student record",parent=self.root)
            else:
                cur.execute("select * from result where roll=? and course=?",(self.var_roll.get(),self.var_course.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Result already present",parent=self.root)
                else:
                    
                    cur.execute("insert into result(roll,name,course,marks_ob,full_marks) values(?,?,?,?,?)",(
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_course.get(),
                        self.var_marks_ob.get(),
                        self.var_full_marks.get() 
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Result added successfully",parent=self.root)
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def clear(self):
        self.var_roll.set("Select"),
        self.var_name.set(""),
        self.var_course.set(""),
        self.var_marks_ob.set(""),
        self.var_full_marks.set("")

if __name__=="__main__":
    root=Tk()
    obj=resultClass(root)
    root.mainloop()