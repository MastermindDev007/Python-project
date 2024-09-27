import mysql.connector as m
con = m.connect(host="localhost", user="root", password="", database="pythondb")

cr = con.cursor()

name = input("Enter Your Name : ")
ct = input("Enter Your City : ")
stream = input("Enter Your Stream : ")

try:
    q = "INSERT INTO STD (Name, City, Stream) VALUES (%s, %s, %s)"
    cr.execute(q, (name, ct, stream))  # Correct parameter passing
    if cr.rowcount > 0:
        con.commit()
        print("Inserted")
except Exception as e:
    con.rollback()
    print(e)
