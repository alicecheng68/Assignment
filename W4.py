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

@app.route("/")    #首頁樣式
def home(): 
    return render_template("W4_Test.html")



@app.route('/signin', methods=['POST'])   #用post方法執行Html裡action的signin
def signin():
        account = request.form['Account']
        password = request.form['Password']
        agree = request.form.get('Agree')


        if account == "test" and password == "test123": #如果帳號密碼正確，跳轉到/member畫面
            if agree:  
                session["signIn"]=True 
                return redirect('/member')
            else:
                return redirect("/")
        elif not account or not password:
            if agree:
                return redirect('/error?message=請輸入帳號和密碼') 
            else:
                return redirect("/")
        else:
            if agree:
                return redirect('/error?message=自訂的錯誤訊息')
            else:
                return redirect("/")
@app.route("/member")
def success_page():
            return render_template('success.html')

@app.route("/error")
def error_page():
        message = request.args.get('message')  #Query String找Html的message
        error_message = "帳號或密碼錯誤" if message == "自訂的錯誤訊息" else message
        return render_template('error.html', message=error_message)
@app.route("/signout")
def signout_page():
    session["signIn"]=False   #如果金鑰Flase，登出跳轉至首頁
    return redirect("/")

if __name__ == "__main__":    #首頁路徑
    app.run(port=3000)