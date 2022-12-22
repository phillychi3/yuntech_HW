<?php
//from post data
$account = $_POST['account'];
$password = $_POST['password'];
//data:
// 帳號：9923701 	密碼：1073299
// 帳號：9923702 	密碼：2073299
$data = array(
    '9923701' => '1073299',
    '9923702' => '2073299'
);
//check and post ajax msg
if(isset($account) && isset($password)){
    if($data[$account] == $password){
        echo '登入成功';
    }else{
        echo '帳號或密碼錯誤';
    }
}

?>