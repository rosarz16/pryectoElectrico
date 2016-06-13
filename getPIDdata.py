import mysql.connector
import os

connection = mysql.connector.connect(host='localhost',
                                     user='root',
                                     passwd='rosario',
                                     db='paretodatabase')

cursor = connection.cursor()
a = 1
t0 = 0.3
Ms = 1.6

cursor.execute("SELECT * from paretopruebatabla where a = %s and (Ms between %s-0.001 and %s+0.001) and t0 = %s;",
               (a, Ms, Ms, t0))
resultados = cursor.fetchall()
for resultado in resultados:
        print resultado[0], resultado[5]

