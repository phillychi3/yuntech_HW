<html>

<?php
    session_start();
    if(! isset($_SESSION['number'])) {
        header('Location: index.php');
    }
    $number = $_SESSION["number"];
    $name = $_SESSION["name"];
    $password = $_SESSION["password"];
    echo "<h1>登入成功</h1>";
    echo "學號: $number";
    echo "姓名: $name";
    echo "密碼: $password";
?>
</html>