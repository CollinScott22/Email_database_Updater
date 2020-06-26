"Install pyodbc library with 'pip install pyodbc'"
import pyodbc

email_input = input().split(" ")
email_input = email_input.split(",")
email_list = []
print(email_input)
for i in email_input:
    if '@' in i:
        if'.com' in i or '.org' in i or '.gov' in i:
            email_list.append(i)

connection = pyodbc.connect('Driver={SQL Server};'
                            'Server=Emails\SQLEXPRESS;'
                            'Database=TestDB;'
                            'Trusted_Connection=yes;')

cursor = connection.cursor()

cursor.execute('SELECT * FROM TestDB.dbo.Addresses')

for row in cursor:
    print(row)

for i in email_list:
    cursor.execute(f'''
                  INSERT INTO TestDB.dbo.Addresses(Email_Address)
                  VALUES
                  ({i})
                  (''')