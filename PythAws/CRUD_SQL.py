import MySQLdb


db = MySQLdb.connect("localhost","root","root","vinit" )
#cursor = db.cursor()

def create():
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS Employee")
    sql = "CREATE TABLE Employee (name  varchar(20) ,age  int(2),phone_Number varchar(18)"
    try:
        cursor.execute(sql)
        print("table created")
    except Exception as e:
        print(e)
    #db.close()


def select():
    cursor = db.cursor()
    sql = "select *from emp"
    try:
       cursor.execute(sql)
       results = cursor.fetchall()         #results=7 i.e no. of rows

       for row in results:
          name = row[0]                        #coloumn0
          age = row[1]
          Mob = row[2]

          print( "Name=%s,age=%s,mob_no=%s" % (name,age,Mob))

    except Exception as e:
       print(e)


def insert():
    cursor = db.cursor()
    n=input("enter name")
    a=int(input("enter age"))
    p=input("enter phone no.")

    tup=(n,a,p)
    try:
        sql="insert into emp values(%s, %s , %s)"
        #values = ("snake", "turtle")

        cursor.execute(sql,tup)
        print("data inserted")
    except Exception as e:
        print(e)




    '''sql = """UPDATE animal SET name = %s
               WHERE name = %s
               '''
def update():
    cursor = db.cursor()
    name=input("enter the name of person whose age you want to update")
    age=int(input("enter the age"))
    try:
        tup=(age,name)
        sql = "UPDATE emp SET age=%s WHERE name=%s "

        cursor.execute(sql,tup)
        #db.commit()
        print("1 row data updated")
    except Exception as e:
        print(e)
    #db.close()

def delete():
    cursor = db.cursor()
    name = input("enter the name of person you want to delete")
    tup=(name)
    sql = "DELETE FROM emp WHERE name=%s"
    try:
        cursor.execute(sql,tup)
        #db.commit()
        print("1 row deleted")
    except Exception as e:
        print(e)
    #db.close()
try:
    while True:
            print()
            print("press 1 for  create table")
            print("press 2 for select")
            print("press 3 for insert table")
            print("press 4 for update table")
            print("press 5 for delete table")
            print("press 6 to exit")
            print()
            alpha = int(input("enter your choice"))

            opt={1:create,
                 2:select,
                 3:insert,
                 4:update,
                 5:delete,
                 6:exit
                 }
            opt[alpha]()

except Exception as e:
    print(e)

finally:
    db.close()

