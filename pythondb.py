#first install the module
    #python -m pip install mysql-connector-python  --user

import mysql.connector

con=mysql.connector.connect(
user="ardit700_student",
password='ardit700_student',
host="108.167.140.122",
database="ardit700_pm1database"
)

cursor=con.cursor()
query = cursor.execute("select * from Dictionary where expression ='inlay' ")
#"SELECT * FROM Dictionary WHERE Expression  LIKE 'r%'"
#"SELECT * FROM Dictionary WHERE length(Expression) < 4"
#"SELECT Definition FROM Dictionary WHERE Expression  LIKE 'r%'"
result =cursor.fetchall()

if result:
    print(result)
    print("First result: " , result[0])
else:
    print("there is no such word")