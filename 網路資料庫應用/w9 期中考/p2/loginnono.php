<html>
    <?php
        session_start();
        echo "<h1>login fail</h1>";
        echo "username:".$_SESSION["username"]."</br>";
        echo "error:".$_SESSION["errorwhat"]."</br>";
    ?>
</html>
