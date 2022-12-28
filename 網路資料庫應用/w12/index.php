<?php
$db = 'C:\Users\phill\Documents\coed_thing\yuntech\網路資料庫應用\w12\testdb.accdb';

$conn = new COM('ADODB.Connection');
$conn->Open("Provider=Microsoft.ACE.OLEDB.12.0;Data Source=$db");

$sql = "SELECT * FROM test";
$rs = $conn->Execute($sql);

echo "<table border='1'>";
echo "<tr>";
echo "<td>number</td>";
echo "<td>name</td>";
echo "<td>password</td>";
echo "</tr>";
while(!$rs->EOF) {
    echo "<tr>";
    echo "<td>".$rs->Fields['number']->Value."</td>";
    echo "<td>".$rs->Fields['name']->Value."</td>";
    echo "<td>".$rs->Fields['password']->Value."</td>";
    echo "</tr>";
    $rs->MoveNext();
}



?>