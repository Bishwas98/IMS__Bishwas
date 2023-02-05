from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk ,messagebox
import sqlite3
class categoryclass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | Developed by Bishwas Khatri")
        self.root.config(bg="white")
        self.root.focus_force()
        #---Variiibles----#
        self.var_Category_ID= StringVar()
        self.var_Name= StringVar()

        #------ Title--------
        Label_Title = Label(self.root,text="Manage Product Category",font=("goudy old style",30),background="#184a45",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill= X,padx=20)
        Label_Name= Label(self.root,text=" Enter Category Name",font=("goudy old style",20,"bold"),background="white").place(x=40,y=120)
        
        Text_Entry= Entry(self.root,textvariable=self.var_Category_ID,font=("goudy old style",18),background="light yellow").place(x=50,y=170,width=290)

         #------Button-------- 
        Button_Add= Button(self.root,text="Add",command=self.add,font=("goudy old style",15),background="#4caf50",fg="white").place(x=360,y=170,width=150, height=30)
        
        Button_Delete= Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),background="red",fg="white").place(x=520,y=170,width=150, height=30)


         #---Category Details TreeView ---#

        Category_Frame = Frame(self.root,bd=3,relief=RIDGE)
        Category_Frame.place(x=675,y=60,width=410,height=140)

        scrolly=Scrollbar(Category_Frame,orient=VERTICAL)
        scrollx=Scrollbar(Category_Frame,orient=HORIZONTAL)
        
        self.Category_Table = ttk.Treeview(Category_Frame,columns=("Category_ID","Name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.Category_Table.xview)
        scrollx.config(command=self.Category_Table.yview)

        self.Category_Table.heading("Category_ID",text="Category ID")
        self.Category_Table.heading("Name",text="Name")

        self.Category_Table["show"] = "headings"

        self.Category_Table.column("Category_ID",width=90)
        self.Category_Table.column("Name",width=90)
        self.Category_Table.pack(fill=BOTH,expand=1)
        self.Category_Table.bind("<ButtonRelease-1>",self.get_data)
       
       #----Images---#
        #Image1
        self.im1 = Image.open("E:\Projects\IMS\Images\Operation.png")
        self.im1 = self.im1.resize((500,250),Image.LANCZOS)             #=======Not Working ========#
        self.im1 = ImageTk.PhotoImage(self.im1)  

        self.label_im1 =Label(self.root,image=self.im1,bd=2,relief=RIDGE) 
        self.label_im1.place(x=50, y=220)
        #Image1
        self.im2 = Image.open("E:\Projects\IMS\Images\Operation2.png")
        self.im2 = self.im2.resize((500,250),Image.LANCZOS)
        self.im2 = ImageTk.PhotoImage(self.im2)

        self.label_im2 =Label(self.root,image=self.im2,bd=2,relief=RIDGE) 
        self.label_im2 .place(x=580, y=220) 
        
        self.show()
#--------------------------------------------------------------------------------------------------
    def add(self):
        con=sqlite3.connect(database=r'IMS.db')
        cur=con.cursor()
        try:
            if self.var_Name.get()=="":
                messagebox.showerror("Error","Category must be required",parent=self.root)
            else:
                cur.execute("Select * from Category where Name=?",(self.var_Name.get(),))
                row= cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Category already assigned,try different",parent=self.root)
                else:
                    cur.execute("Insert into Category, Name=?",( self.var_Name.get(),))   
            con.commit()
            messagebox.showerror("Success","Category Added Successfully",parent=self.root)    
            self.show()        
        except Exception as ex:
         messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)   

    def show(self):
        con=sqlite3.connect(database=r'IMS.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from Category")
            row=cur.fetchall()
            self.Category_Table.delete(*self.Category_Table.get_children())
            for row in row:
                self.Category_Table.insert('',END,values=row)
        except Exception as ex:
         messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def get_data(self,ev):
        f = self.Category_Table.focus()
        content=(self.Category_Table.item(f))
        row=content['values'],
        self.var_Category_ID.set(row[0]),
        self.var_Name.set(1), 


    def delete(self):
        con=sqlite3.connect(database=r'IMS.db')
        cur=con.cursor()
        try: 
            if self.var_Category_ID.get()=="":
                messagebox.showerror("Error","Please select or enter category from the list",parent=self.root)
            else:
                cur.execute("Select * from Category where Category_ID=?",(self.var_Category_ID.get(),))
                row= cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Error! Please try again",parent=self.root)
                else:
                    op= messagebox.askyesno("Confirm","Do you want to delete the Category?",parent=self.root)
                    if op==True:
                        cur.execute("Delete from Category where Category_ID=?",(self.var_Category_ID.get(),))
                        con.commit()
                        messagebox.showinfo("Deleted","Category delete successfully",parent=self.root) 
                        self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)    
    
    def clear(self):
        self.var_Category_ID.set("")
        self.var_Name.set("")
        self.show()

if __name__ == "__main__":
    root = Tk()
    object = categoryclass(root)
    root.mainloop()       