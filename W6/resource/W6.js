function login() {
  let username =document.forms["signinForm"]["username"]
  let password =document.forms["signinForm"]["password"]
  if (username === "" || password === "")
    return false
  const AgreeCheckbox = document.getElementById("agree");
    if (! AgreeCheckbox.checked){
      alert("請勾選同意條款");
      return false; // 取消表單提交
    }}

function signup() {
  let name =document.forms["signupForm"]["name"]
  let username =document.forms["signupForm"]["username"]
  let password =document.forms["signupForm"]["password"]
  if (name===""|| username === "" || password === "")
    return false
}

