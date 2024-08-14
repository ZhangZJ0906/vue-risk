<?php
header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: POST');
header('Access-Control-Allow-Headers: Content-Type');

// 設定文件路徑
$file_path = __DIR__ . '/data.json';



// 等待文件被創建
$attempts = 10;
while ($attempts > 0) {
    if (file_exists($file_path)) {
        http_response_code(200);
        echo json_encode(["message" => "File exists"]);
        exit;
    }
    sleep(1);
    $attempts--;
}

// 如果文件仍不存在，返回 404
http_response_code(404);
echo json_encode(["message" => "File not found"]);
