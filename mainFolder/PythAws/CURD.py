import MySQLdb


db = MySQLdb.connect("localhost","root","root","vinit" )
#cursor = db.cursor()

def create():
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS Employee")
    sql = "CREATE TABLE Employee (FIRST_NAME  CHAR(20) NOT NULL,LAST_NAME  CHAR(20),AGE INT)"
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

          print( "Name=%s,age=%d,mob_no=%s" % (name,age,Mob))

    except:
       print("Error: unable to fecth data")
    #db.close()

def insert():
    cursor = db.cursor()
    sql = "insert into emp(name,age,phone_Number)values('alok',20,'9910998576')"
    try:
        cursor.execute(sql)
        #db.commit()
        print("data inserted")
    except Exception as e:
        print(e)
    #db.close()

def update():
    cursor = db.cursor()
    sql = "UPDATE emp SET name='ram' WHERE phone_Number=9910905576"
    try:
        cursor.execute(sql)
        #db.commit()
        print("1 row data updated")
    except Exception as e:
        print(e)
    #db.close()

def delete():
    cursor = db.cursor()
    sql = "DELETE FROM emp WHERE AGE > '%d'" % (25)
    try:
        cursor.execute(sql)
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

