<?php
header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: GET, POST, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type');

$file_path = __DIR__ . '/data.json';

if (file_exists($file_path)) {
    echo file_get_contents($file_path);
} else {
    http_response_code(404);
    echo json_encode(["message" => "File not found"]);
}
?>
