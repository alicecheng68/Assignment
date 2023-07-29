function login() {
  const AgreeCheckbox = document.getElementById("agree");
    if (! AgreeCheckbox.checked){
      alert("請勾選同意條款");
      return false; // 取消表單提交
    }}