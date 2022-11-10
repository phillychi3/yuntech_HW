<html>
    <head>
        <form>
            學號:<input type="text" name="number" /></br>
            密碼:<input type="text" name="passwords" /></br>
            <input type="submit" value="送出" />
            <input type="reset" value="清除" />
        </form>

    </head>
    <body>
    </body> 
    <?php
        session_start();
        //load scpre.dat
        $ddata = file("C:\Users\phill\Desktop\codes\yuntech_HW\網路資料庫應用\w8\score.dat");
        $number = $_GET["number"];
        $passwords = $_GET["passwords"];
        $data = [];
        //read ddata to data
        foreach($ddata as $line){
            $step[] = explode(" ", $line);
            array_push($data, array('number' => $step[0][0], 'passwords' => $step[0][1], 'chinese' => $step[0][3], 'math' => $step[0][4], 'english' => $step[0][5]));
        }
        //check number and passwords
        foreach($data as $line){
            echo $line['number'];
            echo $line['passwords'];
            if($line['number'] == $number && $line['passwords'] == $passwords){
                $_SESSION["login"] = true;
                $_SESSION['number'] = $number;
                $_SESSION['passwords'] = $passwords;
                $_SESSION['chinese'] = $line['chinese'];
                $_SESSION['math'] = $line['math'];
                $_SESSION['english'] = $line['english'];
                //cookie login_count + 1
                if(!isset($_COOKIE[$number])) {
                    setcookie($number, 1, time() + (86400 * 7), "/");
                } else {
                    setcookie($number, $_COOKIE[$number] + 1, time() + (86400 * 7), "/");
                }
                header('Location: loginsuccess.php');
                break;
            }
        }
        print_r($_SESSION);
        //login fail
        if($number != null && $passwords != null && $_SESSION["login"] != true){
            $_SESSION["login"] = false;
            header('Location: loginfail.php');
        }


        






    ?>
</html>