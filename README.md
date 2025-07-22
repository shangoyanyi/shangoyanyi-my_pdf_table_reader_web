# PDF表格擷取工具
這是一個基於 Pandas、Flask 的小工具，一鍵上傳 PDF、依指定欄位擷取表格內容並匯出成 Excel，支援本地與雲端執行。

## 使用方式
### 本地端使用
1. 安裝 python 3.7 版以上
2. 安裝相依性套件：雙擊執行 install_requirements.bat (會自動透過 pip 安裝所有必要套件)
3. 啟動應用程式：雙擊執行 run_app.bat (會自動啟動本機 Flask Server，開啟預設瀏覽器頁面)
4. 使用流程：在web畫面中選擇待讀取的 pdf 檔案 → 點「轉換」→ 程式會將讀取結果匯出為 output.xlsx，並自動下載

### 發佈到 Render.com
在 Render.com 建立一個新的 Web Service，並依照以下指示設定：
   1. 連結您的儲存庫：將 Render 連接到您存放專案的 GitHub/GitLab 儲存庫。
   2. 填寫設定：
       * Environment: Python 3
       * Build Command: pip install -r requirements.txt
       * Start Command: gunicorn app:app
  完成以上設定後，Render 就會根據您的程式碼和這些指令來建置並啟動您的應用程式。