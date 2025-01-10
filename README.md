# README

## 功能
依據傳入的PDF檔案擷取檔案內的table資料

## 使用方式
### 方式1. 本地執行
1. 執行 run_app.py
2. 在web畫面中選擇待讀取的 pdf 檔案並上傳
3. 點「轉換」
4. 程式會將讀取結果匯出為 output.xlsx，並自動下載

### 方式2. 安裝到Render
1. 建立 GitHub 存儲庫：將專案資料夾上傳到 GitHub。
2. 連結 Render：
    (1) 登錄 Render。
    (2) 選擇 New + Web Service。
    (3) 連結您的 GitHub 存儲庫。
3. 設定 Render 部署：
    (1) 選擇 Python 為運行環境。
    (2) 確保 Render 使用的 Python 版本與您本地一致（如 3.8 或更高）。
    (3) Render 會自動檢測並安裝 requirements.txt 中的所有模組。
4. 啟動應用：部署成功後，Render 會提供一個公共 URL，您可以通過該 URL 訪問您的應用。