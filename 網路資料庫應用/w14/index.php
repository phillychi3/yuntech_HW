<!DOCTYPE html>
<html>
<head>
    <title>資料庫管理系統</title>
    <meta charset="utf-8">
</head>
<body>
    <form method="POST">
        <?php
        $mysql = mysqli_connect("localhost", "root", "", "customer");
        switch ($_POST['page'] ?? 0) {
            case 'search':
                echo "<h2>資料庫管理系統-查詢</h2><hr>";
                echo "<input type='hidden' name='page' value='search'>";
                if (isset($_POST['search-result']) && $_POST['search-result'] == "true") { //result page
                    echo "客戶代號: " . $_POST['search-cust_no'] . "<br>";
                    $result = null;
                    if (is_numeric($_POST['search-cust_no']))
                        $result = mysqli_query($mysql,  "SELECT * FROM basic WHERE cust_no = " . $_POST['search-cust_no'])->fetch_array();
                    if (!is_null($result)) {
                        echo "姓名: " . $result[1] . "<br>";
                        echo "統一編號: " . $result[2] . "<br>";
                        echo "電話號碼: " . $result[4] . "<br>";
                        echo "地址: " . $result[3] . "<br>";
                    } else {
                        echo "<br><label style='color: red;'>！資料不存在！</label><br>";
                    }
                    echo "<br><button type='submit' name='page' value='search'>回查詢畫面</button> ";
                } else { //default page                    
                    echo "客戶代號: <input type='text' name='search-cust_no'/><br><br>";
                    echo "<button type='submit' name='search-result' value='true'>查詢</button> ";
                    echo "<button type='reset' >清除</button> ";
                }
                echo "<button type='submit' name='page' value=''>回主畫面</button><br>";
                break;
            case 'add':
                echo "<h2>資料庫管理系統-新增</h2><hr>";
                echo "<input type='hidden' name='page' value='add'>";
                if (isset($_POST['add-result']) && $_POST['add-result'] == "true") {  //result page
                    $result = false;
                    try {
                        if (is_numeric($_POST['add-cust_no']))
                            $result = mysqli_query($mysql, "INSERT INTO basic(cust_no,name,id,address,tel_no) VALUE('" . $_POST['add-cust_no'] . "','" . $_POST['add-name'] . "','" . $_POST['add-id'] . "','" . $_POST['add-address'] . "','" . $_POST['add-tel_no'] . "')");
                    } catch (Exception) {
                        $result = false;
                    }
                    if ($result) {
                        echo "<br><label>！資料新增成功！</label><br>";
                    } else {
                        echo "<br><label style='color: red;'>！資料新增失敗！</label><br>";
                    }
                    echo "<br><button type='submit' name='page' value='add'>回新增畫面</button> ";
                } else { //default page     
                    echo "客戶代號: <input type='text' name='add-cust_no'/><br>";
                    echo "姓名: <input type='text' name='add-name'/><br>";
                    echo "統一編號: <input type='text' name='add-id'/><br>";
                    echo "電話號碼: <input type='text' name='add-tel_no'/><br>";
                    echo "地址: <input type='text' name='add-address'/><br><br>";
                    echo "<button type='submit' name='add-result' value='true'>新增</button> ";
                    echo "<button type='reset' >清除</button>";
                }
                echo "<button type='submit' name='page' value=''>回主畫面</button><br>";
                break;
            case 'modify':
                echo "<h2>資料庫管理系統-修改</h2><hr>";
                echo "<input type='hidden' name='page' value='modify'>";
                if (isset($_POST['modify-result']) && $_POST['modify-result'] == "true") {  //result page                    
                    echo "客戶代號: " . $_POST['modify-cust_no'] . "<br>";
                    $result = null;
                    if (is_numeric($_POST['modify-cust_no']))
                        $result = mysqli_query($mysql,  "SELECT * FROM basic WHERE cust_no = " . $_POST['modify-cust_no'])->fetch_array();
                    if (!is_null($result)) {
                        echo "<input type='hidden' name='modify-cust_no' value='" . $result[0] . "'/>";
                        echo "姓名: <input type='text' name='modify-name' value='" . $result[1] . "'/><br>";
                        echo "統一編號: <input type='text' name='modify-id' value='" . $result[2] . "'/><br>";
                        echo "電話號碼: <input type='text' name='modify-tel_no' value='" . $result[4] . "'/><br>";
                        echo "地址: <input type='text' name='modify-address' value='" . $result[3] . "'/><br><br>";
                        echo "<button type='submit' name='modify-result2' value='true'>修改</button> ";
                    } else {
                        echo "<br><label style='color: red;'>！資料不存在！</label><br><br>";
                    }
                    echo "<button type='submit' name='page' value='modify'>回修改主畫面</button> ";
                } elseif (isset($_POST['modify-result2']) && $_POST['modify-result2'] == "true") {  //result2 page
                    $result = false;
                    try {
                        if (is_numeric($_POST['modify-cust_no']))
                            $result = mysqli_query($mysql, "UPDATE basic SET name='" . $_POST['modify-name'] . "',id='" . $_POST['modify-id'] . "',address='" . $_POST['modify-address'] . "',tel_no='" . $_POST['modify-tel_no'] . "' WHERE cust_no=" . $_POST['modify-cust_no']);
                    } catch (Exception) {
                        $result = false;
                    }
                    if ($result) {
                        echo "<br><label>！資料修改成功！</label><br><br>";
                    } else {
                        echo "<br><label style='color: red;'>！資料修改失敗！</label><br><br>";
                    }
                    echo "<button type='submit' name='page' value='modify'>回修改主畫面</button> ";
                } else { //default page  
                    echo "客戶代號: <input type='text' name='modify-cust_no'/><br><br>";
                    echo "<button type='submit' name='modify-result' value='true'>查詢</button> ";
                    echo "<button type='reset' >清除</button> ";
                }
                echo "<button type='submit' name='page' value=''>回主畫面</button><br>";
                break;
            case 'delete':
                echo "<h2>資料庫管理系統-刪除</h2><hr>";
                echo "<input type='hidden' name='page' value='delete'>";
                if (isset($_POST['delete-result']) && $_POST['delete-result'] == "true") {  //result page
                    echo "客戶代號: " . $_POST['delete-cust_no'] . "<br>";
                    $result = null;
                    if (is_numeric($_POST['delete-cust_no']))
                        $result = mysqli_query($mysql,  "SELECT * FROM basic WHERE cust_no = " . $_POST['delete-cust_no'])->fetch_array();
                    if (!is_null($result)) {
                        echo "<input type='hidden' name='modify-cust_no' value='" . $result[0] . "'/>";
                        echo "姓名: " . $result[1] . "<br>";
                        echo "統一編號: " . $result[2] . "<br>";
                        echo "電話號碼: " . $result[4] . "<br>";
                        echo "地址: " . $result[3] . "<br>";
                        echo "<label style='color: red;'>是否真的要刪除?</label>";
                        echo " <button type='submit' name='delete-result2' value='true'>是</button> ";
                        echo "<button type='submit' name='delete-result3' value='true'>否</button><hr></form></body></html>";
                        exit();
                    } else {
                        echo "<br><label style='color: red;'>！資料不存在！</label><br>";
                    }
                    echo "<br><button type='submit' name='page' value='delete'>回刪除主畫面</button> ";
                } elseif (isset($_POST['delete-result2']) && $_POST['delete-result2'] == "true") {  //result2 page
                    $result = false;
                    try {
                        if (is_numeric($_POST['modify-cust_no']))
                            $result = mysqli_query($mysql, "DELETE FROM basic WHERE cust_no=" . $_POST['modify-cust_no']);
                    } catch (Exception) {
                        $result = false;
                    }
                    if ($result) {
                        echo "<br><label>！資料刪除成功！</label><br><br>";
                    } else {
                        echo "<br><label style='color: red;'>！資料刪除失敗！</label><br><br>";
                    }
                    echo "<button type='submit' name='page' value='delete'>回刪除主畫面</button> ";
                } elseif (isset($_POST['delete-result3']) && $_POST['delete-result3'] == "true") {  //result3 page
                    echo "<br><label>！資料沒有刪除！</label><br><br>";
                    echo "<button type='submit' name='page' value='delete'>回刪除主畫面</button> ";
                } else { //default page  
                    echo "客戶代號: <input type='text' name='delete-cust_no'/><br><br>";
                    echo "<button type='submit' name='delete-result' value='true'>查詢</button> ";
                    echo "<button type='reset' >清除</button> ";
                }
                echo "<button type='submit' name='page' value=''>回主畫面</button><br>";
                break;
            default:
                echo "<h2>資料庫管理系統</h2><hr>";
                echo "1. <button type='submit' name='page' value='search'>查詢</button><br>";
                echo "2. <button type='submit' name='page' value='add'>新增</button><br>";
                echo "3. <button type='submit' name='page' value='modify'>修改</button><br>";
                echo "4. <button type='submit' name='page' value='delete'>刪除</button><br>";
                break;
        }
        ?>
        <hr>
    </form>
</body>
</html>