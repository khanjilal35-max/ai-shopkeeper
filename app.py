from flask import Flask, request

app = Flask(__name__)

def ai_reply(message):
    message = message.lower()

    if "দাম" in message or "price" in message:
        return "আমাদের পণ্যের দাম জানতে কোন পণ্যটি চান, সেটির নাম লিখুন।"

    if "অর্ডার" in message or "order" in message:
        return "অর্ডার করতে আপনার নাম, মোবাইল নম্বর, ঠিকানা এবং কোন পণ্য চান তা লিখুন।"

    if "হ্যালো" in message or "hello" in message or "hi" in message:
        return "আসসালামু আলাইকুম! 😊 আমাদের পেজে আপনাকে স্বাগতম। কীভাবে সাহায্য করতে পারি?"

    if "ডেলিভারি" in message or "delivery" in message:
        return "ডেলিভারি সংক্রান্ত তথ্য জানতে আপনার এলাকার নাম লিখুন।"

    return "আপনার মেসেজটি পেয়েছি। 😊 একটু বিস্তারিত লিখুন, তাহলে আপনাকে সাহায্য করতে পারব।"


@app.route("/", methods=["GET", "POST"])
def home():
    reply = ""

    if request.method == "POST":
        message = request.form.get("message", "")
        reply = ai_reply(message)

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>AI Shopkeeper</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                max-width: 600px;
                margin: 40px auto;
                padding: 20px;
            }}

            h1 {{
                text-align: center;
            }}

            input {{
                width: 100%;
                padding: 14px;
                box-sizing: border-box;
                margin-bottom: 10px;
            }}

            button {{
                width: 100%;
                padding: 14px;
                cursor: pointer;
            }}

            .reply {{
                margin-top: 20px;
                padding: 15px;
                background: #f1f1f1;
                border-radius: 10px;
            }}
        </style>
    </head>

    <body>
        <h1>🤖 AI Shopkeeper</h1>

        <form method="POST">
            <input
                type="text"
                name="message"
                placeholder="কাস্টমারের মেসেজ লিখুন"
                required
            >
            <button type="submit">উত্তর দেখুন</button>
        </form>

        <div class="reply">
            {reply}
        </div>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
