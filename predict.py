import os
import google.generativeai as genai

# 1. Gemini の設定
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# 2. モデルの指定（最も標準的な名前に戻します）
model = genai.GenerativeModel('gemini-1.5-flash')

# 3. サンプルデータ
race_data = "住之江10R: 1枠小池, 2枠木下, 3枠上條, 4枠橋口, 5枠中越, 6枠谷本"

# 4. AI に予想させる
try:
    # 指示文
    prompt = f"競艇予想のプロとして、以下のデータから的中率重視で3連単3点を選び、その根拠を短く教えてください。：{race_data}"
    
    # 予想生成
    response = model.generate_content(prompt)
    prediction_text = response.text.replace('\n', '<br>')
    
except Exception as e:
    # 万が一エラーが出た場合、原因を特定しやすくします
    prediction_text = f"予想取得中にエラーが発生しました。詳細: {str(e)}"

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
        h1 {{ color: #0077b6; font-size: 1.5em; }}
    </style>
</head>
<body>
    <div class="card">
        <h1>AI競艇予想 (自動更新)</h1>
        <hr>
        <div class="bet">{prediction_text}</div>
        <hr>
        <p style="font-size: 12px; color: #888;">※この予想はAIが自動で生成しています。</p>
    </div>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)
