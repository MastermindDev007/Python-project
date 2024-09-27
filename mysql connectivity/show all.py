import mysql.connector as m
from tabulate import tabulate

# Establish connection
con = m.connect(host="localhost", user="root", password="", database="pythondb")
cr = con.cursor()

try:
    # SQL query to select all records
    q = "SELECT * FROM STD"
    cr.execute(q)

    # Fetch all results from the query
    res = cr.fetchall()

    if res:  # Check if there are any records
        # Get the column names from the cursor description
        columns = [desc[0] for desc in cr.description]

        # Display results in a table format using tabulate
        print(tabulate(res, headers=columns, tablefmt="grid"))
    else:
        print("No records found.")

    print("All records fetched successfully.")

except Exception as e:
    print(f"Error: {e}")

finally:
    cr.close()  # Ensure cursor is closed
    con.close()  # Ensure connection is closed
