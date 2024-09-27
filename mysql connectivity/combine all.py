import mysql.connector as m
from tabulate import tabulate


def insert_record():
    con = m.connect(host="localhost", user="root", password="", database="pythondb")
    cr = con.cursor()
    name = input("Enter Your Name: ")
    ct = input("Enter Your City: ")
    stream = input("Enter Your Stream: ")

    try:
        q = "INSERT INTO STD (Name, City, Stream) VALUES (%s, %s, %s)"
        cr.execute(q, (name, ct, stream))
        if cr.rowcount > 0:
            con.commit()
            print("Inserted successfully.")
    except Exception as e:
        con.rollback()
        print(e)
    finally:
        cr.close()
        con.close()


def update_record():
    con = m.connect(host="localhost", user="root", password="", database="pythondb")
    cr = con.cursor()
    id = int(input("Enter Your Unique ID: "))

    try:
        q = "SELECT * FROM STD WHERE Id = %s"
        cr.execute(q, (id,))
        res = cr.fetchone()

        if res:
            name = input("Enter Your Name: ")
            ct = input("Enter Your City: ")
            stream = input("Enter Your Stream: ")
            q = "UPDATE STD SET Name = %s, City = %s, Stream = %s WHERE Id = %s"
            cr.execute(q, (name, ct, stream, id))

            if cr.rowcount > 0:
                con.commit()
                print("Updated successfully.")
            else:
                print("No changes made.")
        else:
            print("Record not found.")
    except Exception as e:
        con.rollback()
        print(f"Error: {e}")
    finally:
        cr.close()
        con.close()


def delete_record():
    con = m.connect(host="localhost", user="root", password="", database="pythondb")
    cr = con.cursor()
    id = int(input("Enter Your Unique ID: "))

    try:
        q = "DELETE FROM STD WHERE Id = %s"
        cr.execute(q, (id,))

        if cr.rowcount > 0:
            con.commit()
            print("Data deleted successfully.")
        else:
            print("No data deleted. Record may not exist.")
    except Exception as e:
        con.rollback()
        print(f"Error: {e}")
    finally:
        cr.close()
        con.close()


def display_records():
    con = m.connect(host="localhost", user="root", password="", database="pythondb")
    cr = con.cursor()

    try:
        q = "SELECT * FROM STD"
        cr.execute(q)
        res = cr.fetchall()

        if res:
            columns = [desc[0] for desc in cr.description]
            print(tabulate(res, headers=columns, tablefmt="grid"))
        else:
            print("No records found.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cr.close()
        con.close()


def search_records():
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


def main():
    while True:
        print("\nMenu:")
        print("1. Insert Record")
        print("2. Update Record")
        print("3. Delete Record")
        print("4. Display Records")
        print("5. Search Records")
        print("6. Exit")

        choice = int(input("Choose an option (1-6): "))

        if choice == 1:
            insert_record()
        elif choice == 2:
            update_record()
        elif choice == 3:
            delete_record()
        elif choice == 4:
            display_records()
        elif choice == 5:
            search_records()
        elif choice == 6:
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
