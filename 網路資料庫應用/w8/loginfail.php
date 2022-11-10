<html>

    <?php
        session_start();
        if(! isset($_SESSION['login'])) {
            header('Location: index.php');
        }
        $number = $_SESSION["number"];
        echo "學號: $number";
        if($_SESSION["login"] == true) {
            echo "你已經登入成功了 在想啥?";
            
        }
        else{
            echo "login fail";
            echo "<a href='index.php'>重新登入</a>";
        }
    ?>
</html>