import os
from google import genai

# APIキーを読み込む
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# 予想用データ
race_data = "住之江10R: 1枠小池, 2枠木下, 3枠上條, 4枠橋口, 5枠中越, 6枠谷本"

try:
    # AIに予想させる（最新の正しい書き方）
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=f"競艇予想のプロとして、以下のデータから的中率重視で3連単3点を選び、その根拠を短く教えてください。：{race_data}"
    )
    prediction_text = response.text.replace('\n', '<br>')
except Exception as e:
    prediction_text = f"エラーが発生しました: {str(e)}"

# index.html を作成
html_content = f"""
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>AI競艇的中ナビ</title>
</head>
<body style="text-align:center; background:#f0f4f8; padding:20px;">
    <div style="background:white; padding:20px; border-radius:15px; max-width:500px; margin:auto; box-shadow:0 4px 6px rgba(0,0,0,0.1);">
        <h1>AI競艇予想 (Cloudflare完全版)</h1>
        <hr>
        <div style="text-align:left; color:#e63946; font-weight:bold; line-height:1.6;">{prediction_text}</div>
    </div>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)
