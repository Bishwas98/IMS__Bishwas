from  tkinter import*              #--widget Install 
from PIL import Image, ImageTk     #-- PIP instal Pillow for image ralated files
from employee import employeeClass
from supplier import supplierclass
from category import categoryclass
class IMS:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System | Developed by Bishwas Khatri Poudel")
        self.root.config(bg="White")

        #---Titile----#
        self.Logo= Image.open("E:\Projects\IMS\Images\logo.png")
        self.Logo= self.Logo.resize((50,50),Image.ANTIALIAS)
        self.Logo= ImageTk.PhotoImage(self.Logo)
        # self.icon_title=PhotoImage (file="images/Logo.png")
        title = Label(self.root,text="Inventory Management System",image=self.Logo,compound=LEFT,font=("times New Roman",40,"bold"),background="#010c48",foreground="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

        #---Button_Logout---1
        Button_logout= Button(self.root,text="Logout",font=("times new roman",15,"bold"),background="yellow",cursor="hand1").place(x=1150,y=10,height=40,width=150)
        #---Clock---#
        self.lebal_clock= Label(self.root,text="Welcome to Inventory Management System\t\t Date: DD-MM-YY\t\t Time: HH\MM\SS",font=("times New Roman",15),background="#4d636d",foreground="white")
        self.lebal_clock.place(x=0,y=70,relwidth=1,height=30) 

        #---Left Menu---#
        self.MenuLogo= Image.open("E:\Projects\IMS\Images\Menu.png")
        self.MenuLogo= self.MenuLogo.resize((200,100),Image.ANTIALIAS)
        self.MenuLogo= ImageTk.PhotoImage(self.MenuLogo)

        LeftMenu= Frame(self.root,bd=2,relief=RIDGE,background="White")
        LeftMenu.place(x=0 ,y=102,width=200,height=595)

        Label_MenuLogo = Label(LeftMenu,image=self.MenuLogo)
        Label_MenuLogo.pack(side=TOP,fill=X)

        #---Menu Lebal---#
        Label_menu= Label(LeftMenu,text="Menu",font=("times new roman",20,"bold"),background="light blue").pack(side=TOP,fill=X)
        #---Left Menu Button---#
        self.Icon= Image.open("E:\Projects\IMS\Images\icon.png")
        self.Icon= self.Icon.resize((20,20),Image.ANTIALIAS)
        self.Icon= ImageTk.PhotoImage(self.Icon)
        Button_Employee= Button(LeftMenu,text="Employee",command=self.employee,image=self.Icon,compound=LEFT,padx=5,anchor="w",font=("times new roman",20),background="#1A76D7",bd=3,cursor="hand1").pack(side=TOP,fill=X)
        Button_Supplier= Button(LeftMenu,text="Supplier",command=self.supplier, image=self.Icon,compound=LEFT,padx=5,anchor="w",font=("times new roman",20),background="#1A76D7",bd=3,cursor="hand1").pack(side=TOP,fill=X)
        Button_Category= Button(LeftMenu,text="Category",command=self.category,image=self.Icon,compound=LEFT,padx=5,anchor="w",font=("times new roman",20),background="#1A76D7",bd=3,cursor="hand1").pack(side=TOP,fill=X)
        Button_Product= Button(LeftMenu,text="Product",image=self.Icon,compound=LEFT,padx=5,anchor="w",font=("times new roman",20),background="#1A76D7",bd=3,cursor="hand1").pack(side=TOP,fill=X)
        Button_Sales= Button(LeftMenu,text="Sales",image=self.Icon,compound=LEFT,padx=5,anchor="w",font=("times new roman",20),background="#1A76D7",bd=3,cursor="hand1").pack(side=TOP,fill=X)
        Button_Exit= Button(LeftMenu,text="Exit",image=self.Icon,compound=LEFT,padx=5,anchor="w",font=("times new roman",20),background="#1A76D7",bd=3,cursor="hand1").pack(side=TOP,fill=X)
        #---Content---#
        self.Lebal_Employee=Label(self.root,text="Total Employee\n[0]",bd=5,relief=RIDGE,background="#33bbf9",foreground="white",font=("goudy old style",20,"bold"))
        self.Lebal_Employee.place(x=250,y=120,height=150,width=300) 

        self.Lebal_Supplier=Label(self.root,text="Total Supplier\n[0]",bd=5,relief=RIDGE,background="#33bbf9",foreground="white",font=("goudy old style",20,"bold"))
        self.Lebal_Supplier.place(x=600,y=120,height=150,width=300) 

        self.Lebal_Category=Label(self.root,text="Total Category\n[0]",bd=5,relief=RIDGE,background="#33bbf9",foreground="white",font=("goudy old style",20,"bold"))
        self.Lebal_Category.place(x=950,y=120,height=150,width=300) 

        self.Lebal_Product=Label(self.root,text="Total Product\n[0]",bd=5,relief=RIDGE,background="#33bbf9",foreground="white",font=("goudy old style",20,"bold"))
        self.Lebal_Product.place(x=250,y=300,height=150,width=300)

        self.Lebal_Sales=Label(self.root,text="Total Sales\n[0]",bd=5,relief=RIDGE,background="#33bbf9",foreground="white",font=("goudy old style",20,"bold"))
        self.Lebal_Sales.place(x=600,y=300,height=150,width=300) 

        

        #--Footer---#
        Label_Footer=Label(self.root,text="IMS Information Management System | Developed by Bishwas Khatri Poudel | For Any Technical Support call at 9817418311",font=("times new roman",15),background="#4d636d",foreground="white").pack(side=BOTTOM,fill=X)
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def employee(self):
        self.new_win = Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)

    def supplier(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = supplierclass(self.new_win) 

    def category(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = categoryclass(self.new_win)        

if __name__ =="__main__":
    root=Tk()
    object = IMS(root)
root.mainloop() 