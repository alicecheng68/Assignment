import mysql.connector
#連線到資料庫
con=mysql.connector.connect(
    user="root",
    password="@alice0608",
    host="localhost",
    database="website"
)
print("成功")

#建立Cursor物件，用來對資料庫下SQL指令
cursor=con.cursor()
cursor.execute('Insert into member (name,username,password,follower_count) values("Kelly","kelly","testkelly",999) ')
con.commit()   #確定執行

con.close()   #關閉程式

