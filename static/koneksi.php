<?php
 $conn = mysqli_connect("localhost", "root", "", "db_feroution");


 function query($query) {
    global $conn;
    $result1 = mysqli_query($conn, $query);
    $rows = [];
    while ($row = mysqli_fetch_assoc($result1)){

        $rows[] = $row;
    }
    return $rows;
 }


 function submitproduk($produk) {
    $query ="SELECT * FROM mytable WHERE label = '$produk'";


    return query($query);
 }
?>

