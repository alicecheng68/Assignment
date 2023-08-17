from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session
from flask import jsonify
import mysql.connector


app=Flask(
    __name__,
    static_folder="resource",  #靜態資料夾
    static_url_path="/"  #靜態資料夾路徑
)

app.secret_key="any string but secret"  #設定session的密鑰

con=mysql.connector.connect(
    user="root",
    password="12345678",
    host="localhost",
    database="website",
    
)
#建立Cursor物件，用來對資料庫下SQL指令
cursor=con.cursor()

@app.route("/")    # 首頁樣式
def home():
    return render_template("home.html")

@app.route('/signup', methods=['POST'])
def signup_page():
    #從前端接收資料
    name = request.form["name"]
    username = request.form["username"]
    password = request.form["password"]

    #根據接收到的資料，和資料庫互動
    #檢查member表單裡的username
    cursor.execute("SELECT * FROM member WHERE username = %s", (username,))
    orginaluser = cursor.fetchone()   

    if orginaluser:
        return redirect('/error?message=帳號已經被註冊')
    else:
        cursor.execute('Insert into member (name, username, password) VALUES (%s, %s, %s)', (name, username, password))
        con.commit()   #確定執行（新增資料到資料庫）
        return render_template("home.html")
    

@app.route('/signin', methods=['POST'])   # 用 POST 方法執行 Html 裡 action 的 signin
def signin():
    username = request.form['Username']
    password = request.form['Password']

    cursor.execute("SELECT * FROM member WHERE username = %s AND password = %s", (username, password))
    member = cursor.fetchone()  #把取出的資料放到member

    if member: 
        session["signIn"] = True  # 金鑰正確
        session["userId"]=member[0]   #紀錄member第0項資料id
        session["userName"]=member[2]
        session["Name"]=member[1]
        
        return redirect("/member")   # 如果帳號密碼正確，跳轉到 /member 畫面
    elif not username or not password:
        return redirect('/error?message=請輸入帳號和密碼') 
    else:
        return redirect('/error?message=帳號密碼輸入錯誤')
    

@app.route("/member")
def member_page():
    if session.get("signIn"):    #隨時確認金鑰是否為True
        cursor.execute("select member.name, message.content, message.id from member inner join message on member.id=message.member_id order by message.time desc")
        allmessage=cursor.fetchall()
        
        return render_template('member.html',allMessage=allmessage)
    else:
        return redirect("/signout")
    
@app.route("/api/member")
def api_member():
    if session.get("signIn"):    #隨時確認金鑰是否為True
        username = request.args.get('username')  # Query String找Html的username
        cursor.execute("select* from member where username=%s",(username,))
        member=cursor.fetchone()  #找username符合的member資料
        if member:                #找到member資料後輸出
            memberData={
                "data":{
                "id":member[0],
                "name":member[1],
                "username":member[2],
            } }
        else:
            memberData={
                "data":None
            } 
        return jsonify(memberData)


  
    

@app.route("/createMessage", methods=['POST'])
def create_message():
    if session.get("signIn"):    #隨時確認金鑰是否為True
        content=request.form["content"]   #讀取member.html的name="content"
        member_id=session.get("userId")   #member_id=金鑰中的userId
        cursor.execute('INSERT INTO message (member_id, content) VALUES (%s, %s)', (member_id, content))
        con.commit()   #新增留言＆確定執行
        return redirect('/member')
    else:
        return redirect("/signout")
    


@app.route("/error")
def error_page():
    message = request.args.get('message')  # Query String找Html的message
    error_message = "帳號或密碼錯誤" if message == "自訂的錯誤訊息" else message
    return render_template('error.html', message=error_message)




@app.route("/signout")
def signout_page():
    session["signIn"] = False   # 如果金鑰為 False，登出跳轉至首頁
    session.clear()  #清空session所有資料
    return redirect("/")



if __name__ == "__main__":    # 首頁路徑
    app.run(port=3000)

