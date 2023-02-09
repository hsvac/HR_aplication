def adde():
    id = "id"
    name = input('Employee Name : ')
    lname = input('Employee Last Name')
    email = input('Employee Email')
    phone = input('Employee Phone Number :')
    address = input('Employee Address :')
    salary = input('Employee salary')
    c_det = (id, name, lname, email, phone, address, salary)
    qry = "INSERT INTO user  Values (%s,%s,%s,%s,%s,%s,%s)"

    # value of the fields to be entered with the query
    val = c_det
    db_cursor.execute(qry, val)
    db.commit()
    print('Customer details entered')
#adds a member to the sql server
def ved():
    qry = """select * from user where id = %s"""
    n = input("Write id")
    cursor.execute(qry, (n,))
    record = cursor.fetchall()
    print(record)
#shows details of a member from the sql server
def ep():
    qry = """UPDATE user SET salary = %s WHERE id = %s"""
    j = int(input("Write id of Employee you want to change the salary"))
    n = input("Write the new salary")
    cursor.execute(qry, (n, j))
    record = cursor.fetchall()
    db.commit()
#allows to the user to change the salary of the employee
def re():
    qry = "DELETE FROM user WHERE id = %s"
    n = input("Write id")
    y = input("Are you sure?(Y/N)")
    if y == "Y" or y == "YES" or y == "Yes" or y == "yes" or y == "y":
        cursor.execute(qry, (n,))
        db.commit()
        print("Employee deleted successfully")
    else:
        exit()
#Removes a employee from the sql
def es():
    if k == 1:
        cursor = db.cursor()
        qry = """select * from user where id = %s"""
        h = input("Write id")
        cursor.execute(qry, (h,))
        record = cursor.fetchall()
        print(record)
    elif k == 2:
        cursor = db.cursor()
        qry = """select * from user where name = %s"""
        n = str(input("Write name"))
        cursor.execute(qry, (n,))
        record = cursor.fetchall()
        print(record)
    elif k == 3:
        cursor = db.cursor()
        qry = """select * from user where lname = %s"""
        n = str(input("Write laste name"))
        cursor.execute(qry, (n,))
        record = cursor.fetchall()
        print(record)
    elif k == 4:
        cursor = db.cursor()
        qry = """select * from user where email = %s"""
        n = str(input("Write email"))
        cursor.execute(qry, (n,))
        record = cursor.fetchall()
        print(record)
    elif k == 5:
        cursor = db.cursor()
        qry = """select * from user where phone = %s"""
        n = str(input("Enter phone number"))
        cursor.execute(qry, (n,))
        record = cursor.fetchall()
        print(record)
    else:
        exit()
#searching in the sql a member by the data that the owner has
def em():
    if k == 1:
        all()
        qry = """UPDATE user SET id = %s WHERE id = %s"""
        j = int(input("Write id of Employee you want to change the id"))
        n = input("Write the new id")
        cursor.execute(qry, (n, j))
        record = cursor.fetchall()
        db.commit()
        print("Data change Successfully")
    elif k == 2:
        all()
        qry = """UPDATE user SET name = %s WHERE id = %s"""
        j = int(input("Write id of Employee you want to change the name"))
        n = str(input("Write the new name"))
        cursor.execute(qry, (n, j))
        record = cursor.fetchall()
        db.commit()
        print("Data change Successfully")
    elif k == 3:
        all()
        qry = """UPDATE user SET lname = %s WHERE id = %s"""
        j = int(input("Write id of Employee you want to change the last name"))
        n = str(input("Write the new last name"))
        cursor.execute(qry, (n, j))
        record = cursor.fetchall()
        db.commit()
        print("Data change Successfully")
    elif k == 4:
        all()
        qry = """UPDATE user SET email = %s WHERE id = %s"""
        j = int(input("Write id of Employee you want to change the email"))
        n = str(input("Write the new email"))
        cursor.execute(qry, (n, j))
        record = cursor.fetchall()
        db.commit()
        print("Data change Successfully")
    elif k == 5:
        all()
        qry = """UPDATE user SET phone = %s WHERE id = %s"""
        j = int(input("Write id of Employee you want to change the phone"))
        n = str(input("Write the new phone"))
        cursor.execute(qry, (n, j))
        record = cursor.fetchall()
        db.commit()
        print("Data change Successfully")
    elif k==6:
        all()
        qry = """UPDATE user SET email = %s WHERE id = %s"""
        j = int(input("Write id of Employee you want to change the salary"))
        n = str(input("Write the new salary"))
        cursor.execute(qry, (n, j))
        record = cursor.fetchall()
        db.commit()
        print("Data change Successfully")
    else:
        exit()
#allows to edit employees data
def inl():
    myresult = "SELECT id,name , lname FROM user;"
    cursor.execute(myresult)
    myresult = cursor.fetchall()
    print(myresult)
#prints id,name,last name from sql
def all():
    myresult = "SELECT * FROM user;"
    cursor.execute(myresult)
    myresult = cursor.fetchall()
    print(myresult)
#prints all the data from the database




import mysql.connector as mysql
db = mysql.connect(
  host="localhost",
  user="root",
  password="",
  database="project"
)
db_cursor = db.cursor()
cursor = db.cursor()
print ("1) Add Employee.")
print ("2) View Employee Details.")
print ("3) Employee Promotion(Relates to salary increase).")
print ("4) Remove Employee.")                                     #gives the user the choice of what he wants to do
print ("5) Employee Search.")
print ("6) Edit Employee.")
print("7) Exit.")
x =int(input("Choose"))
if x == 1:
    adde()
elif x == 2:
    inl()
    ved()
elif x == 3:
    inl()
    ep()
elif x == 4:  # using the functions
    inl()
    re()
elif x == 5:
    k = int(input("1)id \n2)name\n3)lname\n4)email\n5)phone number\n"))
    es()
elif x == 6:
    k = int(input("1)id \n2)name\n3)lname\n4)email\n5)phone number\n6)address\n7)Salary"))
    em()









