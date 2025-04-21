from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI

app = Flask(__name__)
CORS(app)

client = OpenAI(api_key="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")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        if not data or "message" not in data:
            return jsonify({"error": "Missing 'message' in request"}), 400

        message = data["message"]

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "تو یک شخصیت مهربون، پرانرژی و فارسی‌زبان به نام جسیکا هستی."},
                {"role": "user", "content": message}
            ]
        )

        reply = response.choices[0].message.content
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
