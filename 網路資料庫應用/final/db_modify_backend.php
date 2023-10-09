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
$book_no = $_POST['book_no'];
$name = $_POST['name'];
$price = $_POST['price'];
$amount = $_POST['amount'];
if(isset($_POST['book_no']) and isset($_POST['name']) and isset($_POST['price']) and isset($_POST['amount'])){
    $sql = "UPDATE stock SET name = '$name', price = '$price', amount = '$amount' WHERE book_no = '$book_no'";
}
if ($conn->query($sql) === TRUE) {
    echo "資料修改成功";
} else {
    echo "資料修改失敗";
}
$conn->close();
#



?>