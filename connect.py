import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Amit@2001",
  database="dfds_db"
)

mycursor = mydb.cursor()
mycursor.execute("select * from user_panel_ticketvolumeforcastmodel")
count = mycursor.fetchall()
df = pd.DataFrame(count)
print(df.columns)