<?php
 $conn = mysqli_connect("localhost", "root", "", "db_feroution");


 function query($query) {
    global $conn;
    $result = mysqli_query($conn, $query);
    $rows = [];
    while ($row = mysqli_fetch_assoc($result)){

        $rows[] = $row;
    }
    return $rows;
 }


 function submit($label) {
    $query ="SELECT * FROM mytable WHERE label = '$label'";


    return query($query);
 }
?>

