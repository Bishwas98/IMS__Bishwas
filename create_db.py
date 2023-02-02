import  sqlite3
def create_db():
    con= sqlite3.connect(database=r'IMS.db')
    cur= con.cursor() 
    cur.execute("CREATE TABLE IF NOT EXISTS Employee(Emp_ID INTEGER PRIMARY KEY AUTOINCREMENT,Name text,Email text,Gender text,Contact text,DOB text,DOJ text,Pass text,User_Type text,Address text,Salary text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS Supplier(Invoice INTEGER PRIMARY KEY AUTOINCREMENT,Name text,Contact text,Description text)")
    con.commit()  

    cur.execute("CREATE TABLE IF NOT EXISTS Supplier(Category INTEGER PRIMARY KEY AUTOINCREMENT,Name text)")
    con.commit()  
create_db()   