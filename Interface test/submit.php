<?php
// Get the form data
$client_id = $_POST['client-id'];
$client_secret = $_POST['client-secret'];
$mind = $_POST['mind'];
$memorable = $_POST['memorable'];
$sleep = $_POST['sleep'];
$challenging = $_POST['challenging'];
$advice = $_POST['advice'];

// Format the form data as a CSV row
$row = array($client_id, $client_secret, $mind, $memorable, $sleep, $challenging, $advice);
$row = implode(',', $row) . "\n";

// Write the CSV row to the file
$file = 'form_data.csv';
if (!file_exists($file)) {
    $header = "Client ID,Client Secret,Mind,Memorable,Sleep,Challenging,Advice\n";
    file_put_contents($file, $header);
}
file_put_contents($file, $row, FILE_APPEND);

