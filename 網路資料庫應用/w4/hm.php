<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
</head>
<body>
    <form action="" method="POST">
        <input type="text" name="data" />
        <input type="submit" value="傳送" />
    </form>

    <?php
    $list = array(
        "王一" => array("國文" => 90, "英文" => 100, "數學" => 80),
        "張二" => array("國文" => 82, "英文" => 85, "數學" => 90),
        "Ray" => array("國文" => 80, "英文" => 65, "數學" => 90),
        "KiKi" => array("國文" => 60, "英文" => 85, "數學" => 80),
    );
    function getstudent($data)
    {
        global $list;
        $result = array();
        $sum = 0;
        $count = 0;
        foreach ($list as $key => $value) {
            if ($key == $data) {
                $result = $value;
                foreach ($value as $key => $value) {
                    $sum += $value;
                    $count++;
                }
                $result["總分"] = $sum;
                $result["平均"] = round($sum / $count);
            }
        }
        return $result;
    }
    $psd = $_POST["data"];
    $result = getstudent($psd);
    echo "姓名：" . $psd . "<br>";
    foreach ($result as $key => $value) {
        echo $key . "：" . $value . "<br>";
    }
    if ($result == null) {
        echo "查無此人";
    }
    ?>
</body>
</html>