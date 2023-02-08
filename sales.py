from tkinter import*
from PIL import Image,ImageTk 
from tkinter import ttk, messagebox
import sqlite3 
import os
class salesClass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | Develeped by Bishwas Khatri")
        self.root.config(bg="white")
        self.root.focus_force()
#----------------------------------------------------------------------------------------------------------------------------------------------------------
 
     #---Varible---------------#
        self.var_Invoice = StringVar()
        self.var_Bill_List = []
      
 
     #--Title---
        Label_Title = Label(self.root,text="View Customer Bill",font=("goudy old style",15),background="#0f4d7d",bd=2,relief=RIDGE, foreground="white").pack(side=TOP,fill=X,padx=10,pady=10)
      
        Label_Invoice = Label(self.root,text="Invoice No.",font=("times new roman",15), background="white").place(x=50,y=100)
        Label_Invoice = Entry(self.root,textvariable=self.var_Invoice,font=("times new roman",15),background="light yellow",bd=2,relief=RIDGE).place(x=160,y=100,height=28,width=180)

        Button_Search= Button(self.root,text="Search",command=self.search,font=("times new roman",15,"bold"),background="#2196f3",bd=3,cursor="hand1").place(x=360,y=100,width=128,height=28)
        Button_Clear= Button(self.root,text="Clear",command=self.clear,font=("times new roman",15,"bold"),background="light grey",bd=3,cursor="hand1").place(x=490,y=100,width=128,height=28)
    
    #--Bill List Frame-------------------# 
        Sales_Frame = Frame(self.root,bd=3,relief=RIDGE)
        Sales_Frame.place(x=50,y=140,width=200,height=330)

        Scrolly= Scrollbar(Sales_Frame,orient=VERTICAL)
        self.Sales_List= Listbox(Sales_Frame,font=("goudy old style",15),background="white",yscrollcommand=Scrolly.set)
        Scrolly.pack(side=RIGHT,fill=Y)
        Scrolly.config(command=self.Sales_List.yview)
        self.Sales_List.pack(fill= BOTH,expand =1)

        self.Sales_List.bind("<ButtonRelease-1>",self.get_data)

        #--Bill Area Frame-------------------# 

        Bill_Frame = Frame(self.root,bd=3,relief=RIDGE)
        Bill_Frame.place(x=280,y=140,width=410,height=330)
        
        Label_Title = Label(Bill_Frame,text="Customer Bill Area",font=("goudy old style",15),background="Orange",bd=2,relief=RIDGE, foreground="white").pack(side=TOP,fill=X)


        Scrolly= Scrollbar(Bill_Frame,orient=VERTICAL)
        self.Bill_Area= Listbox(Bill_Frame,font=("goudy old style",15),background="Light yellow",yscrollcommand=Scrolly.set)
        Scrolly.pack(side=RIGHT,fill=Y)
        Scrolly.config(command=self.Bill_Area.yview)
        self.Bill_Area.pack(fill= BOTH,expand =1)

    #---Bill Photo--------------------------#
       
        self.Bill_Photo = Image.open("E:\Projects\IMS\Images\Sales.png")
        self.Bill_Photo = self.Bill_Photo.resize((390,320),Image.LANCZOS)            
        self.Bill_Photo = ImageTk.PhotoImage(self.Bill_Photo)  

        Label_Image = Label(self.root,image=self.Bill_Photo,bd=0)
        Label_Image.place(x=700,y=140)

        self.show()
    #------------------------------------------------------------------------------------------------------------#
        #---OS module---#
    def show(self):
        del self.var_Bill_List[:]
        self.Sales_List.delete(0,END)
        for i in os.listdir('Bill'):
        # print(i.split('.'),i.split('.')[-1]) 
            if i.split('.')[-1]=='txt':
             self.Sales_List.insert(END,i)
             self.var_Bill_List.append(i.split('.')[0])
    
    def get_data(self,ev):
        index_=self.Sales_List.curselection()
        file_name = self.Sales_List.get(index_)
        print(file_name)
        self.Bill_Area.delete('0',END)
        fp=open(f'Bill/{file_name}','r')
        for i in fp:
            self.Bill_Area.insert(END,i)
            fp.close()
    
    def search(self):
        if self.var_Invoice.get()==" ":
            messagebox.showerror("Error","Invoice no. should be required",parent = self.root)
        else:
            if self.var_Invoice.get() in self.var_Bill_List:
                fp=open(f'Bill/{self.var_Invoice.get()}.txt','r')
                self.Bill_Area.delete('0',END)
                for i in fp:
                  self.Bill_Area.insert(END,i)
                fp.close()
            else:
                 messagebox.showerror("Error","Invalid Invocie number.",parent = self.root)

    def clear(self):
        self.show()
        self.Bill_Area.delete('0',END)            

#----------------------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    root = Tk()
    object = salesClass(root)
    root.mainloop() 