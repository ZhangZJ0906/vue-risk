<?php

$logDir = 'backend/';
if (!is_dir($logDir)) {
    mkdir($logDir, 0755, true);
}
$logFile = $logDir . '/api.log';
file_put_contents($logFile, "內容", FILE_APPEND);

