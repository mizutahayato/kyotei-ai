import os
import google.generativeai as genai

# 1. Geminiの設定
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. 本来はここでスクレイピングしますが、まずは「自動更新の流れ」を作るため
# 昨日の住之江4Rのデータをサンプルとして使います
race_data = """
1枠 桑原 将光 (B1) 勝率5.62
2枠 古田 祐貴 (A2) 勝率5.09
3枠 中北 将史 (B1) 勝率4.83
4枠 橋口 真樹 (B1) 勝率4.17
5枠 井内 将太郎 (A2) 勝率6.78
6枠 堀内 亜海 (B2) 勝率1.13
"""

# 3. AIに予想させる
prompt = f"競艇予想のプロとして、以下のデータから的中率重視で3連単3点を選び、その根拠を短く教えてください。データ：{race_data}"
response = model.generate_content(prompt)
prediction_text = response.text

# 4. index.html を自動的に書き換える
html_content = f"""
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI競艇的中ナビ</title>
    <style>
        body {{ font-family: sans-serif; text-align: center; background: #f0f4f8; }}
        .card {{ background: white; margin: 20px auto; padding: 20px; border-radius: 15px; max-width: 400px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }}
        h1 {{ color: #0077b6; }}
        .bet {{ font-size: 20px; font-weight: bold; color: #e63946; white-space: pre-wrap; }}
    </style>
</head>
<body>
    <h1>AI競艇的中ナビ (自動更新中)</h1>
    <div class="card">
        <h2>本日の的中重視予想</h2>
        <div class="bet">{prediction_text}</div>
    </div>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)
