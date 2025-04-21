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
