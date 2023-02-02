from tkinter import*
from PIL import Image,ImageTk 
from tkinter import ttk, messagebox
import sqlite3 
class employeeClass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | Develeped by Bishwas Khatri")
        self.root.config(bg="white")
        self.root.focus_force()

        #---------------------------All Variable Initialized-----------#
        self.var_Searchby = StringVar()
        self.var_Searchtext = StringVar()
        self.var_Employee_Id = StringVar()
        self.var_Gender = StringVar()
        self.var_Contact = StringVar()
        self.var_Name = StringVar()
        self.var_DOB = StringVar()
        self.var_DOJ = StringVar()
        self.var_Email = StringVar()
        self.var_Password = StringVar()
        self.var_Usertype = StringVar()
        self.var_Salary = StringVar()


        #---Searchframe---#
        SearchFrame=LabelFrame(self.root,text="Search Employee",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,background="white")
        SearchFrame.place(x=250,y=20,width=600,height=70)

        #---Option---#
        Combo_Search=ttk.Combobox(SearchFrame,textvariable=self.var_Searchby,values=("Search By","Email","Name","Contact"),state='readonly', justify='center',font=("goudy old style",12))
        Combo_Search.place(x=10,y=5,width=180)
        Combo_Search.current(0)  #values ko index number 0 wata start huncha which is tuple ,so current window start huda select dekheuna current(0) pass gareko ho:

        Entry_Search= Entry(SearchFrame,textvariable=self.var_Searchtext,font=("goudy old style",12),background="light Yellow").place(x=225,y=5,width=160,height=29)
        Button_Search= Button(SearchFrame,text="Search Here!",command=self.Search, font=("goudy old style",12),background="#4caf50",foreground="white",padx=2,cursor="Hand2").place(x=425,y=5,width=160,height=29) 

        #---Title---#
        Title = Label(self.root,text="Employee Details",font=("goudy old style",15),background="#0f4d7d",foreground="white").place(x=50,y=100,width=1000)       
        
        #---Content---#

        #--------------------------Row1-----------------------------#
        #Lebal::
        Label_Employee_ID = Label(self.root,text="Employee ID:",font=("goudy old style",15),background="white").place(x=50,y=150)
        Label_Gender = Label(self.root,text="Gender:",font=("goudy old style",15),background="white").place(x=380,y=150)       
        Label_Contact = Label(self.root,text="Contact:",font=("goudy old style",15),background="white").place(x=680,y=150)    
        #Entry::
        Entrytext_Employee_ID = Entry(self.root,textvariabl=self.var_Employee_Id,font=("goudy old style",12),background="lightyellow").place(x=180,y=150,width=180)
        #ComboBox::
        Combo_Gender=ttk.Combobox(self.root,textvariable=self.var_Gender,values=("","Male","Famle","Other"),state='readonly', justify='center',font=("goudy old style",15))
        Combo_Gender.place(x=460,y=150,width=180) 
        Combo_Gender.current(0)  
        Entrytext_Contact = Entry(self.root,textvariable=self.var_Contact,font=("goudy old style",12),background="lightyellow").place(x=760,y=150,width=205)

        #--------------------------Row2-----------------------------# 
         #Lebal::
        Label_Name = Label(self.root,text="Name:",font=("goudy old style",15),background="white").place(x=50,y=190)
        Label_DOB = Label(self.root,text="D.O.B:",font=("goudy old style",15),background="white").place(x=380,y=190)       
        Label_DOJ = Label(self.root,text="D.O.J:",font=("goudy old style",15),background="white").place(x=680,y=190)    
        #Entry::
        Text_Name=Entry(self.root,textvariabl=self.var_Name,font=("goudy old style",12),background="lightyellow").place(x=180,y=190,width=180)
        Text_DOB=Entry(self.root,textvariabl=self.var_DOB,font=("goudy old style",12),background="lightyellow").place(x=460,y=190,width=180)
        Text_DOJ=Entry(self.root,textvariabl=self.var_DOJ,font=("goudy old style",12),background="lightyellow").place(x=760,y=190,width=205) 

        #--------------------------Row3-----------------------------# 
        #Lebal::
        Label_Email = Label(self.root,text="Email:",font=("goudy old style",15),background="white").place(x=50,y=230)
        Label_Password = Label(self.root,text="Password:",font=("goudy old style",15),background="white").place(x=380,y=230)       
        Label_User_Type = Label(self.root,text="User Type:",font=("goudy old style",15),background="white").place(x=680,y=230)    
        #Entry::
        Text_Email=Entry(self.root,textvariabl=self.var_Email,font=("goudy old style",12),background="lightyellow").place(x=180,y=230,width=180)
        Text_Password=Entry(self.root,textvariabl=self.var_Password,font=("goudy old style",12),background="lightyellow").place(x=470,y=230,width=170)
        Combo_User_Type=ttk.Combobox(self.root,textvariable=self.var_Usertype,values=("","Admin","Employee"),state='readonly', justify='center',font=("goudy old style",15))
        Combo_User_Type.place(x=785,y=230,width=180)
        Combo_User_Type.current(0) 

        #--------------------------Row3-----------------------------# 
        #Lebal::
        Label_Address = Label(self.root,text="Address:",font=("goudy old style",15),background="white").place(x=50,y=270)
        Label_Salary = Label(self.root,text="Salary:",font=("goudy old style",15),background="white").place(x=380,y=270)           
        #Text::
        self.text_address=Text(self.root,font=("goudy old style",12),background="lightyellow")
        self.text_address.place(x=180,y=270,width=180,height=60)
        Text_Salary=Entry(self.root,textvariable=self.var_Salary,font=("goudy old style",12),background="lightyellow").place(x=470,y=270,width=170)    
        
        #Button::
        Button_Save= Button(self.root,text="Save",command=self.add,font=("goudy old style",12),background="#2196f3",foreground="white",cursor="hand2",padx=2).place(x=380,y=305,width=110,height=25) 
        Button_Update= Button(self.root,text="Update",command=self.update, font=("goudy old style",12),background="#4caf50",foreground="white",cursor="hand2",padx=2).place(x=500,y=305,width=110,height=25)
        Button_Delete= Button(self.root,text="Delete",command=self.delete,font=("goudy old style",12),background="#f44336",foreground="white",cursor="hand2",padx=2).place(x=620,y=305,width=110,height=25)
        Button_Clear= Button(self.root,text="Clear",command=self.Clear,font=("goudy old style",12),background="#607d8b",foreground="white",cursor="hand2",padx=2).place(x=740,y=305,width=110,height=25)

        #---Employee Details TreeView ---#

        Employee_Frame = Frame(self.root,bd=3,relief=RIDGE)
        Employee_Frame.place(x=0,y=350,relwidth=1,height=150)

        scrolly=Scrollbar(Employee_Frame,orient=VERTICAL)
        scrollx=Scrollbar(Employee_Frame,orient=HORIZONTAL)
        
        self.EmployeeTable = ttk.Treeview(Employee_Frame,columns=("Emp_ID","Name","Email","Gender","Contact","DOB","DOJ","Pass","User Type","Address","Salary"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrollx.config(command=self.EmployeeTable.yview)

        self.EmployeeTable.heading("Emp_ID",text="Employee ID")
        self.EmployeeTable.heading("Name",text="Name")
        self.EmployeeTable.heading("Email",text="Email")
        self.EmployeeTable.heading("Gender",text="Gender")
        self.EmployeeTable.heading("Contact",text="Contact")
        self.EmployeeTable.heading("DOB",text="DOB")
        self.EmployeeTable.heading("DOJ",text="DOJ")
        self.EmployeeTable.heading("Pass",text="Pass")
        self.EmployeeTable.heading("User Type",text="User Type")
        self.EmployeeTable.heading("Address",text="Adress")
        self.EmployeeTable.heading("Salary",text="Salary")

        self.EmployeeTable["show"] = "headings"

        self.EmployeeTable.column("Emp_ID",width=90)
        self.EmployeeTable.column("Name",width=90)
        self.EmployeeTable.column("Email",width=100)
        self.EmployeeTable.column("Gender",width=100)
        self.EmployeeTable.column("Contact",width=100)
        self.EmployeeTable.column("DOB",width=100)
        self.EmployeeTable.column("DOJ",width=100)
        self.EmployeeTable.column("Pass",width=100)
        self.EmployeeTable.column("User Type",width=100)
        self.EmployeeTable.column("Address",width=100)
        self.EmployeeTable.column("Salary",width=100)
        self.EmployeeTable.pack(fill=BOTH,expand=1)
        self.EmployeeTable.bind("<ButtonRelease-1>",self.get_data)


        self.show()
    #============================================================== 

    def add(self):
        con=sqlite3.connect(database=r'IMS.db')
        cur=con.cursor()
        try:
            if self.var_Employee_Id.get()=="":
                messagebox.showerror("Error","Employe ID must be required",parent=self.root)
            else:
                cur.execute("Select * from Employee where Emp_ID=?",(self.var_Employee_Id.get(),))
                row= cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Employee already assigned,try different",parent=self.root)
                else:
                    cur.execute("Insert into Employee (Emp_ID,Name,Email,Gender,Contact,DOB,DOJ,Pass,User Type,Address,Salary),value(?,?,?,?,?,?,?,?,?,?,?,?)",(
                                              self.var_Employee_Id.get(),
                                              self.var_Name.get(),
                                              self.var_Email.get(),
                                              self.var_Gender.get(),
                                              self.var_Contact.get(),                                      
                                              self.var_DOB.get(),
                                              self.var_DOJ.get(),
                                              self.var_Password.get(),
                                              self.var_Usertype.get(),
                                              self.text_address.get('1.0',END),
                                              self.var_Salary.get()
            ))    
            con.commit()
            messagebox.showerror("Success","Employee Added Successfully",parent=self.root)    
            self.show()        
        except Exception as ex:
         messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)    

    def show(self):
        con=sqlite3.connect(database=r'IMS.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from Employee")
            row=cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in row:
                self.EmployeeTable.insert('',END,values=row)
        except Exception as ex:
         messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def get_data(self,ev):
        f = self.EmployeeTable.focus()
        content=(self.EmployeeTable.item(f))
        row=content['value']
        #print(row)
        self.var_Employee_Id.set(row),
        self.var_Name.set(1),
        self.var_Email.set(2),
        self.var_Gender.set(3),
        self.var_Contact.set(4),                                      
        self.var_DOB.set(5),
        self.var_DOJ.set(6),
        self.var_Password.set(7),
        self.var_Usertype.set(8),
        self.text_address.delete('1.0',END),
        self.text_address.insert(END,row[9]),
        self.var_Salary.set(10)
    

    def update(self):
        con=sqlite3.connect(database=r'IMS.db')
        cur=con.cursor()
        try:
            if self.var_Employee_Id.get()=="":
                messagebox.showerror("Error","Employe ID must be required",parent=self.root)
            else:
                cur.execute("Select * from Employee where Emp_ID=?",(self.var_Employee_Id.get(),))
                row= cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee Id",parent=self.root)
                else:
                    cur.execute("Update Employee set Name=?,Email=?,Gender=?,Contact=?,DOB=?,DOJ=?,Pass=?,User Type=?,Address=?,Salary=? where Emp_ID=?",(                                              
                                              self.var_Name.get(),
                                              self.var_Email.get(),
                                              self.var_Gender.get(),
                                              self.var_Contact.get(),                                      
                                              self.var_DOB.get(),
                                              self.var_DOJ.get(),
                                              self.var_Password.get(),
                                              self.var_Usertype.get(),
                                              self.text_address.get('1.0',END),
                                              self.var_Salary.get(),
                                              self.var_Employee_Id.get(),
            ))    
            con.commit()
            messagebox.showerror("Success","Employee Updated Successfully",parent=self.root)    
            self.show()        
        except Exception as ex:
         messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root) 

    def delete(self):
        con=sqlite3.connect(database=r'IMS.db')
        cur=con.cursor()
        try: 
            if self.var_Employee_Id.get()=="":
                messagebox.showerror("Error","Employe ID must be required",parent=self.root)
            else:
                cur.execute("Select * from Employee where Emp_ID=?",(self.var_Employee_Id.get(),))
                row= cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee Id",parent=self.root)
                else:
                    op= messagebox.askyesno("Confirm","Do you want to delete the record?",parent=self.root)
                    if op==True:
                        cur.execute("Delete from Employee where Emp_Id=?",(self.var_Employee_Id.get(),))
                        con.commit()
                        messagebox.showinfo("Deleted","Employee delete successfully",parent=self.root) 
                        self.Clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
    
    def Clear(self):
        self.var_Employee_Id.set("")
        self.var_Name.set("")
        self.var_Email.set("")
        self.var_Gender.set("Select")
        self.var_Contact.set("")                                      
        self.var_DOB.set("")
        self.var_DOJ.set("")
        self.var_Password.set("")
        self.var_Usertype.set("Admin")
        self.text_address.delete('1.0',END) 
        self.var_Salary.set("")
        self.var_Searchtext.set("") 
        self.var_Searchby.set("Select")
        self.show()

    def Search(self):
        con=sqlite3.connect(database=r"IMS.db")
        cur=con.cursor()
        try:
            if self.var_Searchby.get()=="Select":
                messagebox.showerror("Error","Select Search By option",parent=self.root)
            elif self.var_Searchtext.get()=="":
                messagebox.showerror("Error","Search input should be required",parent=self.root)
            else:
                cur.execute("Select * from Employee"+self.var_Searchby.get()+"LIKE '%"+self.var_Searchtext.get()+"%'")     
                row=cur.fetchall()
                if len(row)!=0:
                    self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                    for row in row:
                        self.EmployeeTable.insert('',END,values=row)
                    else:
                        messagebox.showerror("Error","No record found!!!",parent=self.root)    
        except Exception as ex:
         messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)    


if __name__ == "__main__":
    root = Tk()
    object = employeeClass(root)
    root.mainloop() 