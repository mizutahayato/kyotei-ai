import os
from google import genai

# 1. APIキーの設定
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# 2. 予想用データ
race_data = "住之江10R: 1枠小池, 2枠木下, 3枠上條, 4枠橋口, 5枠中越, 6枠谷本"

# 3. AIに予想させる（モデル名を最新の gemini-2.5-flash に変更）
try:
        response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"競艇のデータアナリストとして、以下のデータから回収率を最大化できる3連単を3点選び、それぞれの買い目に『1万円をどう資金配分して賭けるべきか（例：1-2-3に5000円、など）』まで計算して提示してください。：{race_data}"
    )
    prediction_text = response.text.replace('\n', '<br>')
except Exception as e:
    prediction_text = f"エラーが発生しました: {str(e)}"

# 4. index.html を作成
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
