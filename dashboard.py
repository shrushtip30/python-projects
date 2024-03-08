from tkinter import *
from PIL import Image,ImageTk
from course import CourseClass
from student import studentClass
from result import resultClass
from report import reportClass
class RMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result management system")
        self.root.geometry("1350x750")
        self.root.configure(bg="white")
        #icons
        title=Label(self.root,text="Student Result management System",padx=10,compound=LEFT,font=("arial",20,"bold"),bg="navy blue",fg="white").place(x=0,y=0,relwidth=1,height=50)
        #Menu
        M_Frame=LabelFrame(self.root,text="Menus",font=("times new roman",15),bg="white")
        M_Frame.place(x=10,y=70,width=1340,height=80)
        #buttons
        btn_course=Button(M_Frame,text="Course",font=("times new roman",15,"bold"),bg="light blue",fg="black",cursor="hand2",command=self.add_course).place(x=20,y=5,width=200,height=40)
        btn_student=Button(M_Frame,text="Student",font=("times new roman",15,"bold"),bg="light blue",fg="black",cursor="hand2",command=self.add_student).place(x=240,y=5,width=200,height=40)
        btn_result=Button(M_Frame,text="Result",font=("times new roman",15,"bold"),bg="light blue",fg="black",cursor="hand2",command=self.add_result).place(x=460,y=5,width=200,height=40)
        btn_view=Button(M_Frame,text="View",font=("times new roman",15,"bold"),bg="light blue",fg="black",cursor="hand2",command=self.add_report).place(x=680,y=5,width=200,height=40)
        btn_exit=Button(M_Frame,text="Exit",font=("times new roman",15,"bold"),bg="light blue",fg="black",cursor="hand2").place(x=900,y=5,width=200,height=40)
        #update details
        self.lbl_course=Label(self.root,text="Total Courses\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="orange",fg="white")
        self.lbl_course.place(x=150,y=530,width=300,height=100)
        
        self.lbl_student=Label(self.root,text="Total Students\n[ 0 ]",font=("goudy old style",20),padx=20,bd=10,relief=RIDGE,bg="dark blue",fg="white")
        self.lbl_student.place(x=550,y=530,width=300,height=100)
        
        self.lbl_result=Label(self.root,text="Total Results\n[ 0 ]",font=("goudy old style",20),padx=20,bd=10,relief=RIDGE,bg="green",fg="white")
        self.lbl_result.place(x=950,y=530,width=300,height=100)
        
        #footer
        footer=Label(self.root,text="Student Result management System\nContact us for any technical Issue:987675654",font=("arial",20,"bold"),bg="black",fg="white").pack(side=BOTTOM,fill=X)
    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win)

    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=studentClass(self.new_win)

    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=resultClass(self.new_win)

    def add_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=reportClass(self.new_win)
    
    
if __name__=="__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()
