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
  let username=document.getElementById("inputUsername").value;
  
  fetch(`/api/member?username=${username}`)  
  .then(function(response) {
    return response.json();  // 將回應轉換成 JSON 格式
})  
  .then(function(responseData) {
    let name = document.querySelector("#membername"); //取得html中的id=membername欄位
    if (responseData.data){
      name.innerHTML =`<div>${responseData.data.name} (${responseData.data.username})</div>`;
    }
    else{
      name.innerHTML=`<div>查無此人</div>`;
    }
  });
}

function update_name(){
  let newName = document.getElementById("newName").value;
  fetch("/api/member", {
    method: "PATCH",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        name: newName
    })
})
.then(response => response.json())   //箭頭函示轉換成JSON格式
.then(data => {
    let updateName = document.getElementById("updatename");
    if (data.ok) {
       updateName.innerHTML = `<div>${data.message}</div>`;
    } else {
       updateName.innerHTML = `<div>更新失敗: ${data.message}</div>`;
    }
})
.catch(error => {
    console.error("Error updating name:", error);
});
}
