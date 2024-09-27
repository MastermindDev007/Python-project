import mysql.connector as m

con = m.connect(host="localhost", user="root", password="", database="pythondb")
cr = con.cursor()

id = int(input("Enter Your Unique ID: "))

try:
    # Use parameterized query to avoid SQL injection
    q = "SELECT * FROM STD WHERE Id = %s"
    cr.execute(q, (id,))
    res = cr.fetchone()

    if res:
        name = input("Enter Your Name: ")
        ct = input("Enter Your City: ")
        stream = input("Enter Your Stream: ")

        # Use parameterized query for UPDATE
        q = "UPDATE STD SET Name = %s, City = %s, Stream = %s WHERE Id = %s"
        cr.execute(q, (name, ct, stream, id))

        if cr.rowcount > 0:
            con.commit()
            print("Updated successfully.")
        else:
            print("No changes made.")
    else:
        print("Please insert the record first.")
except Exception as e:
    con.rollback()
    print(f"Error: {e}")
finally:
    cr.close()
    con.close()
