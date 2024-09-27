import mysql.connector as m

# Establish connection
con = m.connect(host="localhost", user="root", password="", database="pythondb")
cr = con.cursor()

id = int(input("Enter Your Unique ID: "))

try:
    # Use parameterized query for DELETE to prevent SQL injection
    q = "DELETE FROM STD WHERE Id = %s"
    cr.execute(q, (id,))

    # Check if any rows were affected
    if cr.rowcount > 0:
        con.commit()
        print("Data deleted successfully.")
    else:
        print("No data deleted. Record with the given ID may not exist.")
except Exception as e:
    con.rollback()  # Rollback in case of an error
    print(f"Error: {e}")
finally:
    cr.close()  # Ensure cursor is closed
    con.close()  # Ensure connection is closed
