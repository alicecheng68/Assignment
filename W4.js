function login() {
    
    const AgreeCheckbox = document.getElementById("agree"); // 取得Html裡同意條款資料
  
    const isChecked = AgreeCheckbox.checked;// 確認是否勾選
  
    
    if (isChecked) {  // 如果已經勾選就可以提交表單到下一步
      const Login = document.getElementById('login');
      Login.submit();
    } else {   // 如果還沒勾選出現警示框
      alert("請勾選同意條款");
    }
  }