<html>
    <body>
        <h2>systemlogin</h2>
        <form action="" method="post">
            <input type="radio" name="login" value="yes">loginsuccess</br>
            <input type="radio" name="login" value="no">loginfail</br>
            <?php
            session_start();
                // if session is new
                if(isset($_SESSION["login"])){
                    echo "<h1> new session: </h1><input type='text' value='no' disabled>";

                }else{
                    echo "<h1> new session: </h1><input type='text' value='yes' disabled>";
                }
            ?>
            </br>
            <input type="submit" value="login">
    </body>
    <?php
        
        $login = $_POST["login"];

        if($login != null){

            if($login == "yes"){
                $_SESSION["login"] = true;
                header("Location: in.php");
            }elseif($login == "no"){
                $_SESSION["login"] = false;
                
            }
            header("Location: in.php");
        }

    ?>
    <style>
        h1{
            display: inline;
        }
    </style>

</html>