<html>
    <body>
        <h1>userdata</h1>
        <form action="" method="post">
            <input type="text" name="name" value="<?php echo isset($_COOKIE["name"]) ? $_COOKIE["name"] : "name" ?>"></br>
            <input type="submit" value="submit">
        </form>
    </body>
    <?php
    $name = $_POST["name"];
    if($name != null){
        setcookie("name", $name);
        setcookie("times", 1, time() + 3600*24*7);
        setcookie("time", date("Y-m-d H:i:s"));
        if($_COOKIE["times"] != null){
            setcookie("times", $_COOKIE["times"]+1, time() + 3600*24*7);
        }
        header("Location: showdata.php");
    }

    ?>
</html>