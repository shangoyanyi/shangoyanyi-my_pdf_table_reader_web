@echo off
:: 設定 CMD 使用 UTF-8
chcp 65001 >nul

:: 設定顯示字型為 Consolas（避免出現 Invalid key name）
reg add "HKCU\Console" /v "FaceName" /t REG_SZ /d "Consolas" /f >nul 2>&1

:: 顯示歡迎訊息
echo ===============================
echo 安裝所有相依性套件
echo ===============================

pip install --retries=1 -r requirements.txt

:: 防止 CMD 視窗閃退
echo ===============================
echo 相依性套件安裝完成。按任意鍵結束...
echo ===============================
pause
