import  sqlite3
def create_db():
    con= sqlite3.connect(database=r'IMS.db')
    cur= con.cursor() 
    cur.execute("CREATE TABLE IF NOT EXISTS Employee(Emp_ID INTEGER PRIMARY KEY AUTOINCREMENT,Name text,Email text,Gender text,Contact text,DOB text,DOJ text,Pass text,User_Type text,Address text,Salary text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS Supplier(Invoice INTEGER PRIMARY KEY AUTOINCREMENT,Name text,Contact text,Description text)")
    con.commit()  

    cur.execute("CREATE TABLE IF NOT EXISTS Category(Category_ID INTEGER PRIMARY KEY AUTOINCREMENT,Name text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS Product(Product_ID INTEGER PRIMARY KEY AUTOINCREMENT,Category text,Supplier text,Product_Name text,Price text,Quantity text,Status text)")
    con.commit()  

create_db()   