from flask import Flask, request, render_template, send_file
from flask_cors import CORS # 導入 CORS
import os
import re
from PyPDF2 import PdfReader
import pandas as pd
from io import BytesIO

# 初始化 Flask 應用程式
app = Flask(__name__)
CORS(app, origins=[
        "http://localhost",
        "http://localhost:5000",
        "http://127.0.0.1",
        "http://127.0.0.1:5000",
        "https://shangoyanyi.github.io"
    ]) # 啟用 CORS，允許特定來源的請求

# 上傳頁面
@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>PDF 轉 CSV 工具</title>
    </head>
    <body>
        <h1>上傳 PDF 並轉換為 CSV</h1>
        <form action="/upload" method="post" enctype="multipart/form-data">
            <label for="file">選擇 PDF 檔案：</label>
            <input type="file" name="file" accept=".pdf" required>
            <button type="submit">轉換</button>
        </form>
    </body>
    </html>
    '''

# 處理文件上傳與轉換
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "錯誤：沒有上傳文件！", 400

    file = request.files['file']
    if file.filename == '':
        return "錯誤：未選擇文件！", 400

    # 保存上傳的 PDF 到暫存目錄
    file_path = os.path.join('temp', file.filename)
    os.makedirs('temp', exist_ok=True)
    file.save(file_path)

    # 提取 PDF 表格數據
    reader = PdfReader(file_path)
    all_data = []
    columns = ["商品料號", "商品名稱", "出貨數", "退貨數", "進出貨數"]

    for page in reader.pages:
        text = page.extract_text()
        rows = re.findall(r'(\d{8,})\s+([\w\W]+?)\s+(\d+)\s+(\d+)\s+(-?\d+)', text)
        for row in rows:
            all_data.append(row)

    # 生成 CSV
    df = pd.DataFrame(all_data, columns=columns)
    output = BytesIO()
    df.to_csv(output, index=False, encoding='utf-8-sig')
    output.seek(0)

    # 清理暫存文件
    os.remove(file_path)

    return send_file(output, mimetype='text/csv', as_attachment=True, download_name='output.csv')

# 啟動應用程式
if __name__ == '__main__':
    app.run(debug=True)
