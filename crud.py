import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
#print(mydb)
mycursor = mydb.cursor()
mycursor.execute("use flight")
mycursor.execute('select * from flight')
data=mycursor.fetchall()
print(data[0][0:5])
