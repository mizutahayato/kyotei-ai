import os
from google import genai

# 1. APIキーの設定
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# 2. あなたがコピーしてくれた本物の最新データ
race_data = """
１		
5323 / B1 香川 陽太 勝率 4.26
２		
3827 / B1 今泉 徹 勝率 4.02
３		
5331 / B1 佐藤 永梧 勝率 4.20
４		
4482 / A1 守屋 美穂 勝率 6.78 (当地勝率 7.83)
５		
3419 / B2 栗原 謙治 勝率 2.50
６		
5471 / B2 田中 結 勝率 0.00
"""

# 3. AIに予想させる（投資・回収率重視スタイル）
try:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"競艇のデータアナリストとして、以下のデータから回収率を最大化できる3連単を3点選び、それぞれの買い目に『1万円をどう資金配分して賭けるべきか（例：1-2-3に5,000円、1-3-2に3,000円など）』まで予算の傾斜配分を論理的に計算して提示してください。特に4枠の守屋美穂選手（A1級・勝率高）の実力が飛び抜けている点や、各枠の勝率の差を考慮してください。：{race_data}"
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
        <h1>AI競艇予想 (最新レース・資金配分モード)</h1>
        <hr>
        <div style="text-align:left; color:#1d3557; font-weight:bold; line-height:1.6;">{prediction_text}</div>
    </div>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)
