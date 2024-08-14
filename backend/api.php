<?php
header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: POST');
header('Access-Control-Allow-Headers: Content-Type');

// 日誌文件
$logFile = 'api.log';
file_put_contents($logFile, "Request received\n", FILE_APPEND);

// 數據庫連接參數
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "fmras_sql";

// 創建連接
$conn = new mysqli($servername, $username, $password, $dbname);

// 檢查連接
if ($conn->connect_error) {
    die(json_encode(["message" => "連接失敗: " . $conn->connect_error]));
}

// 獲取原始 POST 數據
$json = file_get_contents('php://input');
file_put_contents($logFile, "Raw JSON data: $json\n", FILE_APPEND);

$data = json_decode($json, true);
file_put_contents($logFile, "Decoded data: " . print_r($data, true) . "\n", FILE_APPEND);

// 檢查是否通過 POST 方法提交表單
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    file_put_contents($logFile, "POST method confirmed\n", FILE_APPEND);

    // 獲取表單數據
    $company = $data['company'] ?? '';
    $compiled = $data['compiled'] ?? '';

    // 驗證數據
    if (empty($company) || empty($compiled)) {
        echo json_encode(["message" => "公司名稱和公司統編是必填的。"]);
    } else {
        // 插入數據到數據庫
        $stmt = $conn->prepare("INSERT INTO web_input (CompanyName, BusinessAccountingNO) VALUES (?, ?)");
        $stmt->bind_param("ss", $company, $compiled);

        if ($stmt->execute()) {
            
            $output = [];
            $return_var = 0;
            exec("pyy\crow\Scripts\python.exe pyy\main.py", $output, $return_var);

            
            file_put_contents($logFile, "Python 腳本執行結果:\n" . implode("\n", $output) . "\n", FILE_APPEND);

            if ($return_var === 0) {
                echo json_encode(["message" => "數據插入成功,Python 腳本運行成功"]);
            } else {
                echo json_encode(["message" => "數據插入成功,但 Python 腳本運行失敗: 詳情請查看日誌文件"]);
            }
        } else {
            echo json_encode(["message" => "數據插入失敗: " . $stmt->error]);
        }

        // 關閉預處理語句
        $stmt->close();
    }
} else {
    file_put_contents($logFile, "Request method: " . $_SERVER["REQUEST_METHOD"] . "\n", FILE_APPEND);
    echo json_encode(["message" => "請通過表單提交數據。"]);
}

// 關閉數據庫連接
$conn->close();
