import sqllite3

connection=sqlite3.connect("student.db")

##create a cursor 
cursor=connection.cursor()

##create the table
