@echo off
:: 設定 CMD 使用 UTF-8
chcp 65001 >nul
:: 設定顯示字型為支援 Unicode 的字型，例如 Consolas
reg query "HKCU\\Console\\%SystemRoot%_system32_cmd.exe" >nul || reg add "HKCU\\Console\\%SystemRoot%_system32_cmd.exe" /v "FaceName" /t REG_SZ /d "Consolas" /f

:: 顯示歡迎訊息
echo ===============================
echo 啟動 Flask 應用程式
echo ===============================

:: 檢查 Python 是否已安裝
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [錯誤] 未檢測到 Python！請安裝 Python 3.7 或更高版本後再運行此程式。
    echo 下載地址：https://www.python.org/
    pause
    exit /b
)

:: 檢查是否已安裝必要的套件
echo 檢查並安裝必要套件...
pip show flask >nul 2>&1
if %errorlevel% neq 0 (
    echo Flask 未安裝，正在安裝 Flask...
    pip install flask
)

pip show pandas >nul 2>&1
if %errorlevel% neq 0 (
    echo Pandas 未安裝，正在安裝 Pandas...
    pip install pandas
)

pip show pypdf2 >nul 2>&1
if %errorlevel% neq 0 (
    echo PyPDF2 未安裝，正在安裝 PyPDF2...
    pip install pypdf2
)

:: 啟動 Flask 應用程式
echo 啟動 Flask 應用程式中...
start http://127.0.0.1:5000  :: 自動打開預設瀏覽器
python app.py

:: 防止 CMD 視窗閃退
echo ===============================
echo Flask 應用程式已啟動。按任意鍵結束...
pause
