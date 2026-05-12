import os
from google import genai

# APIキー設定
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# 予想用データ
race_data = "住之江10R: 1枠小池, 2枠木下, 3枠上條, 4枠橋口, 5枠中越, 6枠谷本"

try:
    # 命令を client.models.generate_content に完全に修正
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=f"競艇のプロとして的中重視の3連単3点を出して：{race_data}"
    )
    # AIの回答を取得
    prediction_text = response.text.replace('\n', '<br>')
except Exception as e:
    prediction_text = f"エラーが発生しました: {str(e)}"

# HTML作成
html_content = f"""
<!DOCTYPE html>
<html lang="ja">
<head><meta charset="UTF-8"><title>AI競艇</title></head>
<body style="text-align:center; background:#f0f4f8; padding:20px;">
    <div style="background:white; padding:20px; border-radius:15px; max-width:500px; margin:auto;">
        <h1>AI競艇予想 最新版</h1>
        <div style="text-align:left; line-height:1.6;">{prediction_text}</div>
        <p style="font-size:10px; color:gray;">更新時刻: 2026/05/13</p>
    </div>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)
