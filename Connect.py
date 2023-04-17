import pyodbc


class Connect:
    con = pyodbc.connect('Driver={SQL Server};'
                         'Server=SAICHI-SAMA\SQLEXPRESS;'
                         'Datebase = Test;'
                         'Trusted_Connection = yes')

    cursor = con.cursor()
    cursor.execute('SELECT * FROM Client')

    def InsertStaff(self, insertDict):
        con = self.connect
        cur = con.cursor
        query = f"INSERT INTO Client" \
                f"values ('{insertDict['first_name']}'," \
                f"('{insertDict['second_name']}'," \
                f"('{insertDict['last_name']}'," \
                f"('{insertDict['phone_num']}'," \
                f"('{insertDict['email_add']}'," \
                f"('{insertDict['organisation']}',"

        try:
            cur.execute(query)
        except pyodbc.Error as err:
            print("Error", err)
            cur.close()

    def get_staff_all(self):
        con = self.connect
        cur = con.cursor()
        query = f"SELECT * FROM Test"

        try:
            cur.execute(query)
            rows = cur.fetchall()
        except pyodbc.Error as err:
            print("Error", err)
            cur.close()
            return rows

    def get_staff_by_suername(self, name):
        con = self.connect
        cur = con.cursor()
        query = f"SELECT * FROM Client WHERE first_name'" + name + "'"
        try:
            cur.execute(query)
            rows = cur.fetchall()
        except pyodbc.Error as err:
            print("Error", err)
            cur.close()
            return rows
