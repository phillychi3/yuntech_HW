<html>
    <head>

    </head>
    <body>
        <form action="" method="post">
            <input type="text" name="number" />
            <input type="text" name="name" />
            <input type="text" name="password" />
            <input type="submit" value="送出" />
            <input type="reset" value="清除" />
        </form>

    </body>
    <?php
        session_start();
        
        $dbdata = [
            "9923701"=>[
                "name"=>"黃一",
                "password"=>"1073299"
            ],
            "9923702"=>[
                "name"=>"吳二",
                "password"=>"2073299"
            ],
            "111"=>[
                "name"=>"111",
                "password"=>"111"
            ],
        ];
        if($_SESSION["login"] == true) {
            header('Location: loginsuccess.php');
        }

        if(isset($_POST["number"]) && isset($_POST["name"]) && isset($_POST["password"])) {
            $number = $_POST["number"];
            $name = $_POST["name"];
            $password = $_POST["password"];
            $_SESSION["number"] = $number;
            $_SESSION["name"] = $name;
            if($dbdata[$number]["name"] == $name && $dbdata[$number]["password"] == $password) {
                $_SESSION["password"] = $password;
                $_SESSION["login"] = true;
                echo "登入成功";
                header('Location: loginsuccess.php');
                exit();
            } else {
                echo "登入失敗";
                header('Location: loginfail.php');
            }
        }


    ?>
</html>