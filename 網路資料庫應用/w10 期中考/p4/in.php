<?php
    session_start();
    if(isset($_SESSION["login"]) != true){
        header("Location: index.php");
    }
    if($_SESSION["login"] == true){
        echo "<h1>login success</h1>";
    }else{
        echo "<h1>login fail</h1>";
    }
    echo "<a href='clear.php'>back</a>";
    
?>