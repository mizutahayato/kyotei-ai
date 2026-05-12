import os
from google import genai

# 1. 最新のGemini設定
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

# 2. サンプルデータ
race_data = "住之江10R: 1枠小池, 2枠木下, 3枠上條, 4枠橋口, 5枠中越, 6枠谷本"

# 3. AIに予想させる（ここを最新の書き方に修正）
try:
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=f"競艇予想のプロとして、以下のデータから的中率重視で3連単3点を選び、その根拠を短く教えてください。：{race_data}"
    )
    prediction_text = response.text.replace('\n', '<br>')
except Exception as e:
    prediction_text = f"予想取得中にエラーが発生しました。詳細: {str(e)}"

# 4. index.html を作成
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
