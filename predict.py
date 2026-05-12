import os
import google.generativeai as genai

# 1. Geminiの設定
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# 2. モデルの指定（最もエラーが起きにくい最新の記述法に変更）
model = genai.GenerativeModel('gemini-1.5-flash-latest')

# 3. サンプルデータ
race_data = "住之江10R: 1枠小池, 2枠木下, 3枠上條, 4枠橋口, 5枠中越, 6枠谷本"

# 4. AIに予想させる
try:
    prompt = f"競艇予想のプロとして、以下のデータから的中率重視で3連単3点を選び、その根拠を短く教えてください。：{race_data}"
    response = model.generate_content(prompt)
    prediction_text = response.text.replace('\n', '<br>')
except Exception as e:
    # エラーが起きた時に原因がわかるように表示を工夫
    prediction_text = f"AI予想取得エラー。モデル名を再確認してください。詳細: {str(e)}"

# 5. index.html を作成
html_content = f"""
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>AI競艇的中ナビ</title>
    <style>
        body {{ font-family: sans-serif; text-align: center; background: #f0f4f8; padding: 20px; }}
        .card {{ background: white; padding: 20px; border-radius: 15px; max-width: 500px; margin: auto; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }}
        .bet {{ color: #e63946; font-weight: bold; font-size: 1.1em; text-align: left; line-height: 1.6; }}
    </style>
</head>
<body>
    <div class="card">
        <h1>AI競艇予想 (自動更新)</h1>
        <div class="bet">{prediction_text}</div>
    </div>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)
