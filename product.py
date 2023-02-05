from tkinter import*
from PIL import Image,ImageTk 
from tkinter import ttk, messagebox
import sqlite3 
class productClass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | Develeped by Bishwas Khatri")
        self.root.config(bg="white")
        self.root.focus_force()
        
   #-----------------------------------------------Varibale-------------------#
        self.var_Searchby = StringVar()
        self.var_Searchtext = StringVar()
        self.var_List_Category = StringVar()
        self.var_List_Supplier = StringVar()
        self.var_Category =StringVar()
        self.var_Supplier= StringVar()
        
        
        self.var_Product_ID = StringVar()
        self.var_Product_Name = StringVar()
        self.var_Price = StringVar()
        self.var_Qunatity= StringVar()
        self.var_Status =StringVar()
        
   #-------------------------------------------------Frame--------------------#

        Product_Frame= Frame(self.root,background="White",bd=3,relief=RIDGE)
        Product_Frame.place(x=10,y=10,width=450,height=480)

        #--Titile--#
        Title = Label(Product_Frame,text="Manage Product Details",font=("goudy old style",15,"bold"),background="#0f4d7d",foreground="white").pack(side=TOP,fill=X)       
         #--Label--#
        Label_Category = Label(Product_Frame,text="Category:",font=("goudy old style",15),background="White").place(x=30,y=60)
        Label_Supplier = Label(Product_Frame,text="Supplier:",font=("goudy old style",15),background="White").place(x=30,y=110) 
        Label_Product = Label(Product_Frame,text="Product Name:",font=("goudy old style",15),background="White").place(x=30,y=160) 
        Label_Price = Label(Product_Frame,text="Price:",font=("goudy old style",15),background="White").place(x=30,y=210) 
        Label_Quantity = Label(Product_Frame,text="Quantity:",font=("goudy old style",15),background="White").place(x=30,y=260)   
        Label_Status = Label(Product_Frame,text="Status:",font=("goudy old style",15),background="White").place(x=30,y=310) 

        #---COMBO--#
        Combo_Category=ttk.Combobox(Product_Frame,textvariable=self.var_Category,values=("Select"),state='readonly', justify='center',font=("goudy old style",12,"bold"))
        Combo_Category.place(x=180,y=60,width=200)
        Combo_Category.current(0)

        Combo_Supplier=ttk.Combobox(Product_Frame,textvariable=self.var_Supplier,values=("Select"),state='readonly', justify='center',font=("goudy old style",12,"bold"))
        Combo_Supplier.place(x=180,y=110,width=200)
        Combo_Supplier.current(0)  

        Combo_Status=ttk.Combobox(Product_Frame,textvariable=self.var_Status,values=("Active","Inactive"),state='readonly', justify='center',font=("goudy old style",12,"bold"))
        Combo_Status.place(x=180,y=310,width=200)
        Combo_Status.current(0) 
         
        #---EntryField--#
        Entrytext_Name = Entry(Product_Frame,textvariable=self.var_Product_Name,font=("goudy old style",12),background="lightyellow").place(x=180,y=160,width=205)
        Entrytext_Price = Entry(Product_Frame,textvariable=self.var_Price,font=("goudy old style",12),background="lightyellow").place(x=180,y=210,width=205)
        Entrytext_Status = Entry(Product_Frame,textvariable=self.var_Status,font=("goudy old style",12),background="lightyellow").place(x=180,y=260,width=205)
        
        #---Button--#
        Button_Save= Button(Product_Frame,text="Save",command=self.add,font=("goudy old style",12),background="#2196f3",foreground="white",cursor="hand2",padx=2).place(x=5,y=400,width=100,height=40) 
        Button_Update= Button(Product_Frame,text="Update",command=self.update, font=("goudy old style",12),background="#4caf50",foreground="white",cursor="hand2",padx=2).place(x=120,y=400,width=100,height=40)
        Button_Delete= Button(Product_Frame,text="Delete",command=self.delete,font=("goudy old style",12),background="#f44336",foreground="white",cursor="hand2",padx=2).place(x=230,y=400,width=100,height=40)
        Button_Clear= Button(Product_Frame,text="Clear",command=self.clear,font=("goudy old style",12),background="#607d8b",foreground="white",cursor="hand2",padx=2).place(x=340,y=400,width=100,height=40)
    

        #---Searchframe---#
        SearchFrame=LabelFrame(self.root,text="Search Employee",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,background="white")
        SearchFrame.place(x=480,y=10,width=600,height=80)

        #---Option---#
        Combo_Search=ttk.Combobox(SearchFrame,textvariable=self.var_Searchby,values=("Select","Category","Supplier","Product Name"),state='readonly', justify='center',font=("goudy old style",12))
        Combo_Search.place(x=10,y=5,width=180)
        Combo_Search.current(0)  #values ko index number 0 wata start huncha which is tuple ,so current window start huda select dekheuna current(0) pass gareko ho:

        Entry_Search= Entry(SearchFrame,textvariable=self.var_Searchtext,font=("goudy old style",12),background="light Yellow").place(x=225,y=5,width=160,height=29)
        Button_Search= Button(SearchFrame,text="Search Here!",command=self.Search, font=("goudy old style",12),background="#4caf50",foreground="white",padx=2,cursor="Hand2").place(x=425,y=5,width=160,height=29) 


         #---Product Details TreeView ---#

        Product_Frame = Frame(self.root,bd=3,relief=RIDGE)
        Product_Frame.place(x=480,y=100,width=600,height=390)

        scrolly=Scrollbar(Product_Frame,orient=VERTICAL)
        scrollx=Scrollbar(Product_Frame,orient=HORIZONTAL)
        
        self.Product_Table = ttk.Treeview(Product_Frame,columns=("Product_ID","Category","Supplier","Product_Name","Price","Quantity","Status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.Product_Table .xview)
        scrollx.config(command=self.Product_Table .yview)
        self.Product_Table.heading("Product_ID",text="Product_ID")
        self.Product_Table.heading("Category",text="Category")
        self.Product_Table.heading("Supplier",text="Supplier")
        self.Product_Table.heading("Product_Name",text="Product Name")
        self.Product_Table.heading("Price",text="Price")
        self.Product_Table.heading("Quantity",text="Quantity")
        self.Product_Table.heading("Status",text="Status")
        
        self.Product_Table["show"] = "headings"
          
        self.Product_Table.column("Product_ID",width=90)  
        self.Product_Table.column("Category",width=90)
        self.Product_Table.column("Supplier",width=90)
        self.Product_Table.column("Product_Name",width=90)
        self.Product_Table.column("Price",width=90)
        self.Product_Table.column("Quantity",width=90)
        self.Product_Table.column("Status",width=90)
        self.Product_Table.pack(fill=BOTH,expand=1)
        self.Product_Table.bind("<ButtonRelease-1>",self.get_data)


    #------------------------------------Add,Save,Delete,Clear---------------------------------#
    def add(self):
        con=sqlite3.connect(database=r'IMS.db')
        cur=con.cursor()
        try:
            if self.var_List_Category.get()=="Select" or self.var_List_Category.get()=="Empty" or self.var_List_Supplier.get()=="Select" or self.var_List_Supplier.get()=="Empty" or self.var_Product_Name.get()=="" :
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                cur.execute("Select * from Product where Product_ID=?",(self.var_Product_Name.get(),))
                row= cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Product already present,try different",parent=self.root)
                else:
                    cur.execute("Insert into Product(Product_ID,Category,Supplier,Product_Name,Price,Quantity, Status),value(?,?,?,?,?,?)",(
                                              self.var_Product_ID.get(),  
                                              self.var_Category.get(),
                                              self.var_Supplier.get(),
                                              self.var_Product_Name.get(),
                                              self.var_Price.get(),
                                              self.var_Qunatity.get(),
                                              self.var_Status.get(),
                                              
            ))    
            con.commit()
            messagebox.showerror("Success","Product Added Successfully",parent=self.root)    
            self.show()        
        except Exception as ex:
         messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)    

    def show(self):
        con=sqlite3.connect(database=r'IMS.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from Product")
            row=cur.fetchall()
            self.Product_Table.delete(*self.Product_Table.get_children())
            for row in row:
                self.Product_Table.insert('',END,values=row)
        except Exception as ex:
         messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def get_data(self,ev):
        f = self.Product_Table.focus()
        content=(self.Product_Table.item(f))
        row=content['value'],
        self.var_Product_ID.set(row[0]),
        self.var_Category.set(row[1]),
        self.var_Supplier.set(row[2]),
        self.var_Product_Name.set(row[3]),
        self.var_Price.set(row[4]),
        self.var_Qunatity.set(row[5]),
        self.var_Status.set(row[6])                                   
    

    def update(self):
        con=sqlite3.connect(database=r'IMS.db')
        cur=con.cursor()
        try:
            if self.var_Product_ID.get()=="":
                messagebox.showerror("Error","Select from the list.",parent=self.root)
            else:
                cur.execute("Select * from Product where Product_ID=?",(self.var_Product_ID.get(),))
                row= cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Product",parent=self.root)
                else:
                    cur.execute("Update into Product set Category =?,Supplier=?,Product_Name=?,Price=?,Quantity=?,Status=? where Product_ID=?",(                                            
                                            self.var_Category.get(),
                                            self.var_Supplier.get() ,
                                            self.var_Product_Name.get(),
                                            self.var_Price.get(),
                                            self.var_Qunatity.get(),
                                            self.var_Status.get(), 
                                            self.var_Product_ID                                                                         
                                            ))    
            con.commit()
            messagebox.showerror("Success","Product Updated Successfully",parent=self.root)    
            self.show()              

        except Exception as ex:
         messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
         
              

    def fetch_Category_Supplier(self):
        self.var_List_Category.append("Empty")
        self.var_List_Supplier.append("Empty")
        con=sqlite3.connect(database=r'IMS.db')
        cur=con.cursor()
        try: 
           cur.execute("Select Name from Category")
           category=cur.fetchall()
           if len(category)>0:
              del self.var_List_Category[:]
              self.var_List_Category.append("Select")
           for i in category:
            self.var_List_Category.append(i[0])

           cur.execute("Select Name from Supplier")
           supplier =cur.fetchall
           if len(supplier)>0:
              del self.var_List_Supplier[:]
              self.var_List_Supplier.append("Select")
           for i in supplier:
            self.var_List_Supplier.append(i[0])

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)



    def delete(self):
        con=sqlite3.connect(database=r'IMS.db')
        cur=con.cursor()
        try: 
            if self.var_Product_ID.get()=="":
                messagebox.showerror("Error","Product must be required.",parent=self.root)
            else:
                cur.execute("Select * from Employee where Product_ID=?",(self.var_Product_ID.get(),))
                row= cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Product",parent=self.root)
                else:
                    op= messagebox.askyesno("Confirm","Do you want to delete the record?",parent=self.root)
                    if op==True:
                        cur.execute("Delete from Product where Product_ID=?",(self.var_Product_ID.get(),))
                        con.commit()
                        messagebox.showinfo("Deleted","Product delete successfully",parent=self.root) 
                        self.Clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
    
    def clear(self):
        self.var_Category.set("Select"),
        self.var_Supplier.set("Select") ,
        self.var_Product_Name.set(""),
        self.var_Price.set(""),
        self.var_Qunatity.set(""),
        self.var_Status.set("Active"), 
        self.var_Product_ID.set(""),   
       
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
                cur.execute("Select * from Product"+self.var_Searchby.get()+"LIKE '%"+self.var_Searchtext.get()+"%'")     
                row=cur.fetchall()
                if len(row)!=0:
                    self.Product_Table.delete(*self.Product_Table.get_children())
                    for row in row :
                        self.Product_Table.insert('',END,values=row)
                    else:
                        messagebox.showerror("Error","No record found!!!",parent=self.root)    
        except Exception as ex:
         messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)    



if __name__ == "__main__":
    root = Tk()
    object = productClass(root)
    root.mainloop()  