from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

openai.api_key = "sk-..."  # کلید API خودتو اینجا بذار

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
