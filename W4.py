from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session


app=Flask(
    __name__,
    static_folder="resource",  #靜態資料夾
    static_url_path="/"  #靜態資料夾路徑
)

app.secret_key="any string but secret"  #設定session的密鑰

@app.route("/")    # 首頁樣式
def home():
    return render_template("home.html")

@app.route('/signin', methods=['POST'])   # 用 POST 方法執行 Html 裡 action 的 signin
def signin():
    account = request.form['Account']
    password = request.form['Password']

    if account == "test" and password == "test123": # 如果帳號密碼正確，跳轉到 /member 畫面
        session["signIn"] = True  # 金鑰正確

        return redirect("/member")
    elif not account or not password:
        return redirect('/error?message=請輸入帳號和密碼') 
    else:
        return redirect('/error?message=自訂的錯誤訊息')

@app.route("/member")
def success_page():
    if session.get("signIn"):    #隨時確認金鑰是否為True
        return render_template('success.html')
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
    return redirect("/")

if __name__ == "__main__":    # 首頁路徑
    app.run(port=3000)