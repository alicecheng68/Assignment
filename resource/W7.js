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

function lookup_name(){
  let username =document.forms["lookupForm"]["inputUsername"]; 
  
  fetch(`http://127.0.0.1:3000/api/member?username=${username}`)  
  .then(function(memberData) {
    return memberData.json();  // 將回應轉換成 JSON 格式
})  
  .then(function(response) {
    let name = document.quertSelector("#membername")
    name.innerHTML = `<div>${response.data.name} (${response.data.username})</div>`;
    });
}
