<html>
    <?php
    session_start();
    if(! isset($_SESSION['login'])) {
        header('Location: index.php');
    }
    if($_SESSION['login'] == true) {
        //chean session
        $_SESSION['login'] = false;
        $_SESSION['number'] = null;
        $_SESSION['password]'] = null;
        $_SESSION['chinese'] = null;
        $_SESSION['math'] = null;
        $_SESSION['english'] = null;
    }
    header('Location: index.php');


    ?>
</html>