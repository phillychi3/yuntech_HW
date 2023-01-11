<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <title>資料庫搜尋系統</title>
    </head>
    <body>
        <h1>庫存管理系統 新增</h1>
        <form action="" method="post">
            書號<input type="text" name="book_id" /><br>
            書名<input type="text" name="book_name" /><br>
            價格<input type="text" name="book_price" /><br>
            數量<input type="text" name="book_amount" /><br>
            <input type="submit" value="新增" />
            <input type="reset" value="清除" />
        </form>
    </body>
    <style>
        p{
            white-space: nowrap;
        }
    </style>
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
    $book_id = $_POST['book_id'];
    $book_name = $_POST['book_name'];
    $book_price = $_POST['book_price'];
    $book_amount = $_POST['book_amount'];

    if(isset($_POST['book_id']) and isset($_POST['book_name']) and isset($_POST['book_price']) and isset($_POST['book_amount'])){
        $sql = "INSERT INTO stock (book_no, name, price, amount) VALUES ('$book_id', '$book_name', '$book_price', '$book_amount')";
    }
    if ($conn->query($sql) === TRUE
        and isset($_POST['book_id']) and isset($_POST['book_name']) and isset($_POST['book_price']) and isset($_POST['book_amount'])) {
        echo "資料新增成功";
        echo "<button>回新增畫面</button>";
    } else {
        echo "資料新增失敗";
        echo "<button>回新增畫面</button>";
    }

?>
</html>

