# -*- coding: utf-8 -*-
# MySQL Workbench Python script
# <description>
# Written in MySQL Workbench 6.3.6
import mysql.connector
import os 

connection = mysql.connector.connect(host='localhost',
                             user='root',
                             passwd='rosario',
                             db='paretodatabase')

cursor = connection.cursor()

for dirpath, dirsInDirpath, filesInDirPath in os.walk("C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/ParetosX/"):
    for myfile in filesInDirPath:
        path = os.path.join(dirpath, myfile)
        query = "LOAD DATA LOCAL INFILE '" + path + """' INTO TABLE paretopruebatabla FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\\n' IGNORE 1 ROWS;"""
        cursor.execute(query) # {acuerdate de descomentar esto, o no}
connection.commit()
cursor.close()
