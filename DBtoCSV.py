import sqlite3
import os.path
import csv
from os import path

#only works if this python file is in the same directory as the .db file
tables = []
index = 0

database = input("Enter an existing .db file: ") # user input a db file
if(path.exists(str(database)+".db")):
	conn = sqlite3.connect(str(database)+".db") # connects to the database
	c = conn.cursor() 
	c.execute('SELECT name from sqlite_master where type = "table"')
	tableName = c.fetchall() # grabs all table names
	for name in tableName:
		tables.append(name[0])
	while(index != len(tableName)):
		attributes = []
		c.execute("SELECT * FROM " + str(tables[index]) + ";")
		rows = c.fetchall() # grabs all of the tuples
		columns = c.description # grabs all of the attributes
		for j in range(len(columns)): # gets the attribute names
			attributes.append(str(columns[j][0])) # this is how to get all of the attributes
			
		with open(str(tables[index])+".csv","w",newline = "", encoding = 'utf-8') as attrFile: # encoding utf-8 used for special characters
			attrWrite = csv.writer(attrFile, delimiter = ',')
			attrWrite.writerows([attributes])
		attrFile.close()
		for row in rows: #this is how to get the tuple values
			values = []
			for i in range(len(row)):
				# print(str(row[i]))
				values.append(str(row[i])) # each tuple value is appended 
			
			with open(str(tables[index])+'.csv',"a",newline = "", encoding = 'utf=8') as valFile: # encoding utf-8 used for special characters
				valWrite = csv.writer(valFile, delimiter = ',')
				valWrite.writerows([values]) # values must be inserted into a list
			valFile.close()
		index += 1
	c.close()
	conn.close()
	print("Success")
else:
	print("This file does not exist in the current directory") # when the db file does not exist
