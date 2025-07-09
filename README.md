# README

## 功能
依據傳入的PDF檔案擷取檔案內的table資料

## 使用方式
### 本地端使用
1. 執行 run_app.py
2. 在web畫面中選擇待讀取的 pdf 檔案並上傳
3. 點「轉換」
4. 程式會將讀取結果匯出為 output.xlsx，並自動下載

### 發佈到Render.com
在 Render.com 建立一個新的 Web Service，並依照以下指示設定：
   1. 連結您的儲存庫：將 Render 連接到您存放專案的 GitHub/GitLab 儲存庫。
   2. 填寫設定：
       * Environment: Python 3
       * Build Command: pip install -r requirements.txt
       * Start Command: gunicorn app:app
  完成以上設定後，Render 就會根據您的程式碼和這些指令來建置並啟動您的應用程式。