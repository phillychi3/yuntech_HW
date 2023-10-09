<html>

<body>
    <!-- system login -->
    <form action="" method="post">
        <input type="text" name="username" placeholder="username"></br>
        <input type="text" name="password" placeholder="password"></br>
        <input type="submit" value="login">
        <input type="reset" value="clear">
    </form>
</body>
<?php
session_start();
$username = $_POST["username"];
$password = $_POST["password"];
$_SESSION["username"] = $username;
$file = fopen("password.txt", "r");

if ($username != null && $password != null) {

    while (($line = fgets($file)) !== false) {
        $line = explode(" ", $line);

        // // print($line[0] == $username);
        // print($line[1]);
        // // print_r($line[0] == $username && $line[1] == $password);

        if ($line[0] == $username && trim($line[1]) == $password) {
            echo "login success";
            header("Location: loginyes.php");
            break;
        } elseif ($line[0] == $username && $line[1] != $password) {
            $_SESSION["errorwhat"] = "password";
        } elseif ($line[0] != $username && $line[1] == $password) {
            $_SESSION["errorwhat"] = "username";
        } else {
            $_SESSION["errorwhat"] = "username and password";
        }
    }
    fclose($file);

    header("Location: loginnono.php");
}
?>

</html>