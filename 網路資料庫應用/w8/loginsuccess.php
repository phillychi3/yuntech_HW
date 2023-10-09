<html>

<?php
    session_start();
    if($_SESSION['login'] == false) {
        header('Location: index.php');
    }
    $number = $_SESSION["number"];
    $chinese = $_SESSION["chinese"];
    $math = $_SESSION["math"];
    $english = $_SESSION["english"];
    $average = ($chinese + $math + $english) / 3;
    echo '學號 <input type="text" name="number" value="'.$number.'" readonly="readonly" /><br />';
    echo '登入次數 <input type="text" name="login" value="'.$_COOKIE[$number].'" readonly="readonly" /><br />';
    echo '國文 <input type="text" name="chinese" value="'.$chinese.'" readonly="readonly" /><br />';
    echo '數學 <input type="text" name="math" value="'.$math.'" readonly="readonly" /><br />';
    echo '英文 <input type="text" name="english" value="'.$english.'" readonly="readonly" /><br />';
    echo '平均 <input type="text" name="average" value="'.$average.'" readonly="readonly" /><br />';
    echo '<a href="logout.php">登出</a>';
?>
</html>