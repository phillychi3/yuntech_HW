<?php
    $user = $_COOKIE["name"];
    $times = $_COOKIE["times"];
    $time = $_COOKIE["time"];
    echo "<h1>userdata</h1>";
    echo "name:".$user."</br>";
    echo "times:".$times."</br>";
    echo "time:".$time."</br>";

    echo "<a href='index.php'>back</a>";

?>