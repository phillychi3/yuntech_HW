<html>

    <?php
        session_start();
        if(! isset($_SESSION['number'])) {
            header('Location: index.php');
        }
        $number = $_SESSION["number"];
        $name = $_SESSION["name"];
        echo "學號: $number";
        echo "姓名: $name";
        if($_SESSION["login"] == true) {
            echo "你已經登入成功了 在想啥?";
            
        }
        else{
            echo "login fail";
            echo "<a href='index.php'>重新登入</a>";
        }


    ?>
</html>