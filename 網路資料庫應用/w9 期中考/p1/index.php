<html>
    <head>

    </head>
    <body>
        <form action="" method="post">
            姓名:<input type="text" name="name"></br>
            年齡:<input type="text" name="yard"></br>
            性別:<input type="radio" name="type" value="男">男
            <input type="radio" name="type" value="女">女</br>
            出生地:
            <input type="radio" name="born" value="台灣本島">台灣本島
            <input type="radio" name="born" value="外島">外島</br>
            就業情況:
            <select name="thejob">
                <option value="在職中">在職中</option>
                <option value="謀職中">謀職中 </option>
                <option value="學生">學生</option>
                <option value="其他">其他</option>
            </select></br>
            健身方法:
            <input type="checkbox" name="gym[]" value="快走">快走
            <input type="checkbox" name="gym[]" value="跑步">跑步
            <input type="checkbox" name="gym[]" value="游泳">游泳
            <input type="checkbox" name="gym[]" value="太極拳">太極拳</br>
            興趣:</br>
            <select name="hobby[]" multiple>
                <option value="唱歌">唱歌</option>
                <option value="跳舞">跳舞</option>
                <option value="繪畫">繪畫</option>
                <option value="寫作">寫作</option>
            </select></br>
            補充說明:</br>
            <textarea name="text" cols="30" rows="10"></textarea></br>
            <input type="submit" value="送出">
            <input type="reset" value="清除">
        </form>
    </body>
    <?php
        error_reporting(E_ERROR); 
        ini_set("display_errors", "Off");
        $name=$_POST["name"];
        $yard=$_POST["yard"];
        $type=$_POST["type"];
        $born=$_POST["born"];
        $thejob=$_POST["thejob"];
        $gym=$_POST["gym"];
        $gym = implode(",",$gym);
        $hobby=$_POST["hobby"];
        $hobby = implode(",",$hobby);
        $text=$_POST["text"];
        echo "姓名:".$name."</br>";
        echo "年齡:".$yard."</br>";
        echo "性別:".$type."</br>";
        echo "出生地:".$born."</br>";
        echo "就業情況:".$thejob."</br>";
        echo "健身方法:".$gym."</br>";
        echo "興趣:".$hobby."</br>";
        echo "補充說明:".$text."</br>";
        
    ?>
</html>