<html>
    <h1>基本資料管理系統 查詢</h1>
    <form action="index.php" method="post">
        <input type="text" name="no" placeholder="請輸入編號">
        <input type="submit" name="submit" value="查詢">
    </form>
</html>


<?php
    $servername = 'localhost';
    $username = "root";
    $password = "root";
    $dbname = "yuntech";
    $conn = new mysqli($servername, $username, $password, $dbname);
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    $formdata = $_POST['no'];
    if (isset($_POST['submit'])) {
        $sql = "SELECT * FROM testdb WHERE no = '$formdata'";
    }
    $result = $conn->query($sql);
    if ($result->num_rows > 0) {
        while ($row = $result->fetch_assoc()) {
            echo "編號: " . $row["no"] . " - 姓名: " . $row["name"] . " - 地址: " . $row["Address"] . " - 電話: " . $row["Tel"] . " - 生日: " . $row["Birthday"] . " - email: " . $row["email"] . " - 等級" . $row["Proprity"] . "<br>";
        }
    } else {
        echo "資料不存在";
    }

?>