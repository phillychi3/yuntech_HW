<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <title>資料庫搜尋系統</title>
    </head>
    <body>
        <h1>庫存管理系統 查詢</h1>
        <form action="" method="post">
            <p>書號</p><input type="text" name="book_id" /><br>
            <input type="submit" value="查詢" />
            <input type="reset" value="清除" />
        </form>
    </body>
    <?php
    ini_set("display_errors", "On");
    $servername = 'localhost';
    $username = "root";
    $password = "root"; 
    $dbname = "book";
    $conn = new mysqli($servername, $username, $password, $dbname);
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    $formdata = $_POST['book_id'];
    if(isset($_POST['book_id'])){
        $sql = "SELECT * FROM stock WHERE book_no = '$formdata'";
        $result = $conn->query($sql);
    }
    
    if ($result->num_rows > 0) {
        echo "<form action='db_modify_backend.php' method='post'>";
        while ($row = $result->fetch_assoc()) {
            // echo "書號: " . $row["book_no"] . "<br>" . " - 書名: " . $row["name"] . "<br>" . " - 價格: " . $row["price"] . "<br>" . " - 數量" . $row["amount"] . "<br>";
            echo "書號: " . $row["book_no"] . "<br>" ;
            echo "<input type='hidden' name='book_no' value='" . $row["book_no"] . "' /><br>";
            echo "<input type='text' name='name' value='" . $row["name"] . "' /><br>";
            echo "<input type='text' name='price' value='" . $row["price"] . "' /><br>";
            echo "<input type='text' name='amount' value='" . $row["amount"] . "' /><br>";
        }
        echo "<input type='submit' value='修改' />";
        echo "</form>";
        echo "<button>回查詢畫面</button>";


    } else {
        if(isset($_POST['book_id'])){
            echo "書號: " . $formdata . "<br>";
        }
        echo "資料不存在";
        echo "<button>回查詢畫面</button>";
    }   
?>
</html>

