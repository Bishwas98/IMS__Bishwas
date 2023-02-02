from tkinter import*
from PIL import Image,ImageTk 
from tkinter import ttk, messagebox
import sqlite3 
class supplierclass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | Develeped by Bishwas Khatri")
        self.root.config(bg="white")
        self.root.focus_force()

        #---------------------------All Variable Initialized-----------#
        self.var_Searchby = StringVar()
        self.var_Searchtext = StringVar()
        self.var_Supplier_Invoice = StringVar()
        self.var_Contact = StringVar()
        self.var_Name = StringVar()
        self.var_Description= StringVar()
        

        #---Option---#
        Label_Search=Label(self.root,text="Invoice No :", background="White",font=("goudy old style",12,"bold"))
        Label_Search.place(x=650,y=80)
   
        Entry_Search= Entry(self.root,textvariable=self.var_Searchtext,font=("goudy old style",12),background="light Yellow").place(x=750,y=80,width=160,height=29)
        Button_Search= Button(self.root,text="Search Here!",command=self.Search, font=("goudy old style",12),background="#4caf50",foreground="white",padx=2,cursor="Hand2").place(x=920,y=80,width=140,height=29) 

        #---Title---#
        Title = Label(self.root,text="Supplier Details",font=("goudy old style",20,"bold"),background="#0f4d7d",foreground="white").pack(side=TOP,fill=X,padx=20)      
        
        #---Content---#

        #--------------------------Row1-----------------------------#
        #Lebal::
        Label_Supplier_Invoice = Label(self.root,text="Invoice No:",font=("goudy old style",15,),background="white").place(x=50,y=60)           
        Entrytext_Supplier_Invoice = Entry(self.root,textvariabl=self.var_Supplier_Invoice,font=("goudy old style",12),background="lightyellow").place(x=180,y=70,width=180)
               
        #--------------------------Row2-----------------------------# 
         #Lebal::
        Label_Name = Label(self.root,text="Name:",font=("goudy old style",15),background="white").place(x=50,y=100)
        Text_Name=Entry(self.root,textvariabl=self.var_Name,font=("goudy old style",12),background="lightyellow").place(x=180,y=110,width=180)

        #--------------------------Row3-----------------------------# 
        #Lebal::
        Label_Contact = Label(self.root,text="Contact:",font=("goudy old style",15),background="white").place(x=50,y=140)
        Text_Contact=Entry(self.root,textvariabl=self.var_Contact,font=("goudy old style",12),background="lightyellow").place(x=180,y=150,width=180)

        #--------------------------Row4-----------------------------# 
        #Lebal::
        Label_Description = Label(self.root,text="Description:",font=("goudy old style",15),background="white").place(x=50,y=180)         
        Text_Description=Entry(self.root,textvariabl=self.var_Description,font=("goudy old style",12),background="lightyellow").place(x=180,y=190,width=460,height=120)
        
        
        #Button::
        Button_Save= Button(self.root,text="Save",command=self.add,font=("goudy old style",12),background="#2196f3",foreground="white",cursor="hand2",padx=2).place(x=180,y=350,width=100,height=30) 
        Button_Update= Button(self.root,text="Update",command=self.update, font=("goudy old style",12),background="#4caf50",foreground="white",cursor="hand2",padx=2).place(x=295,y=350,width=100,height=30)
        Button_Delete= Button(self.root,text="Delete",command=self.delete,font=("goudy old style",12),background="#f44336",foreground="white",cursor="hand2",padx=2).place(x=415,y=350,width=100,height=30)
        Button_Clear= Button(self.root,text="Clear",command=self.Clear,font=("goudy old style",12),background="#607d8b",foreground="white",cursor="hand2",padx=2).place(x=535,y=350,width=100,height=30)

        #---Supplier Details TreeView ---#

        Supplier_Frame = Frame(self.root,bd=3,relief=RIDGE)
        Supplier_Frame.place(x=650,y=120,width=410,height=350)

        scrolly=Scrollbar(Supplier_Frame,orient=VERTICAL)
        scrollx=Scrollbar(Supplier_Frame,orient=HORIZONTAL)
        
        self.SupplierTable = ttk.Treeview(Supplier_Frame,columns=("Invoice","Name","Contact","Description"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.SupplierTable.xview)
        scrollx.config(command=self.SupplierTable.yview)

        self.SupplierTable.heading("Invoice",text="Invoice No.")
        self.SupplierTable.heading("Name",text="Name")
        self.SupplierTable.heading("Contact",text="Contact")
        self.SupplierTable.heading("Description",text="Description")

        self.SupplierTable["show"] = "headings"

        self.SupplierTable.column("Invoice",width=90)
        self.SupplierTable.column("Name",width=90)
        self.SupplierTable.column("Contact",width=100) 
        self.SupplierTable.column("Description",width=100)
        self.SupplierTable.pack(fill=BOTH,expand=1)
        self.SupplierTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()
    #============================================================== 

    def add(self):
        con=sqlite3.connect(database=r'IMS.db')
        cur=con.cursor()
        try:
            if self.var_Supplier_Invoice.get()=="":
                messagebox.showerror("Error","Invoice must be required",parent=self.root)
            else:
                cur.execute("Select * from Supplier where Invoice=?",(self.var_Supplier_Invoice.get(),))
                row= cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Invoice no. already assigned,try different",parent=self.root)
                else:
                    cur.execute("Insert into Supplier (Invoice,Name,Contact,Description),value(?,?,?,?)",(
                                              self.var_Supplier_Invoice.get(),
                                              self.var_Name.get(),
                                              self.var_Contact.get(),
                                              self.text_Description.get('1.0',END),
            ))    
            con.commit()
            messagebox.showerror("Success","Supplier Added Successfully",parent=self.root)    
            self.show()        
        except Exception as ex:
         messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)    

    def show(self):
        con=sqlite3.connect(database=r'IMS.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from Supplier")
            row=cur.fetchall()
            self.SupplierTable.delete(*self.SupplierTable.get_children())
            for row in row:
                self.SupplierTable.insert('',END,values=row)
        except Exception as ex:
         messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def get_data(self,ev):
        f = self.SupplierTable.focus()
        content=(self.SupplierTable.item(f))
        row=content['value']
        #print(row)
        self.var_Supplier_Invoice.set(row[0]),
        self.var_Name.set(1),
        self.var_Contact.set(2),                                      
        self.text_Description.delete('1.0',END),
        self.text_Description.insert(END,row[3]),
    

    def update(self):
        con=sqlite3.connect(database=r'IMS.db')
        cur=con.cursor()
        try:
            if self.var_Supplier_Invoice.get()=="":
                messagebox.showerror("Error","Invoice no. must be required",parent=self.root)
            else:
                cur.execute("Select * from Supplier where Invoice=?",(self.var_Supplier_Invoice.get(),))
                row= cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Invoice no.",parent=self.root)
                else:
                    cur.execute("Update Supplier set Name=?,Contact=?,Description=? where Invoice=?",(                                              
                                              self.var_Name.get(),
                                              self.var_Contact.get(),                                      
                                              self.text_Description.get('1.0',END),
                                              self.var_Supplier_Invoice.get(),
            ))    
            con.commit()
            messagebox.showerror("Success","Supplier Updated Successfully",parent=self.root)    
            self.show()        
        except Exception as ex:
         messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root) 

    def delete(self):
        con=sqlite3.connect(database=r'IMS.db')
        cur=con.cursor()
        try: 
            if self.var_Supplier_Invoice.get()=="":
                messagebox.showerror("Error","Invoice no. must be required",parent=self.root)
            else:
                cur.execute("Select * from Supplier where Invoice=?",(self.var_Supplier_Invoice.get(),))
                row= cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Invoice no.",parent=self.root)
                else:
                    op= messagebox.askyesno("Confirm","Do you want to delete the Invoice?",parent=self.root)
                    if op==True:
                        cur.execute("Delete from Supplier where Invoice=?",(self.var_Supplier_Invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Deleted","Supplier delete successfully",parent=self.root) 
                        self.Clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
    
    def Clear(self):
        self.var_Supplier_Invoice.set("")
        self.var_Name.set("")
        self.var_Contact.set("")
        self.text_Description.delete('1.0',END) 
        self.var_Searchtext.set("") 
        self.show()

    def Search(self):
        con=sqlite3.connect(database=r"IMS.db")
        cur=con.cursor()
        try:            
            if self.var_Searchtext.get()=="":
                messagebox.showerror("Error","Invoice no. should be required",parent=self.root)
            else:
                cur.execute("Select * from Supplier where Invoice=?",(self.var_Searchtext.get(),))    
                row=cur.fetchone()
                if row!=None:
                    self.SupplierTable.delete(*self.SupplierTable.get_children())
                    self.SupplierTable.insert(''.END,values=row)
                    for row in row:
                        self.SupplierTable.insert('',END,values=row)
                    else:
                        messagebox.showerror("Error","No record found!!!",parent=self.root)    
        except Exception as ex:
         messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)    


if __name__ == "__main__":
    root = Tk()
    object = supplierclass(root)
    root.mainloop() 