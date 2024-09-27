import mysql.connector as m
from tabulate import tabulate

con = m.connect(host="localhost", user="root", password="", database="pythondb")
cr = con.cursor()

print("Search by: ")
print("1. Id")
print("2. Name")
print("3. City")
print("4. Stream")
option = int(input("Choose an option (1-4): "))

fields = {
    1: "Id",
    2: "Name",
    3: "City",
    4: "Stream"
}

if option in fields:
    search_field = fields[option]
    search_value = input(f"Enter {search_field}: ")

    try:
        if option == 1:
            q = f"SELECT * FROM STD WHERE {search_field} = %s"
            cr.execute(q, (int(search_value),))
        else:
            q = f"SELECT * FROM STD WHERE {search_field} LIKE %s"
            cr.execute(q, (f"%{search_value}%",))

        res = cr.fetchall()

        if res:
            columns = [desc[0] for desc in cr.description]
            print(tabulate(res, headers=columns, tablefmt="grid"))
        else:
            print(f"No records found for {search_field}: {search_value}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        cr.close()
        con.close()

else:
    print("Invalid option. Please choose a valid field.")
