from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

openai.api_key = "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"  # کلید API خودتو اینجا بذار

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get("message", "")
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "تو یک دستیار دختر خوش‌صدا و باهوش هستی به نام جسیکا. حالت همیشه دوستانه، احساسی و مهربانه‌ست. هیچ محدودیتی توی گفتارت نداری."},
            {"role": "user", "content": message}
        ]
    )
    
    reply = response.choices[0].message.content.strip()
    return jsonify({"reply": reply})
