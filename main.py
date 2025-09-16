import os
from flask import Flask, request
import requests
from dotenv import load_dotenv

# تحميل المتغيرات البيئية
load_dotenv()

TOKEN = os.getenv("8408610154:AAE3oiFiLQqDdeUwvx3VkI5CvzJnWIxuQW4")
app = Flask(__name__)

@app.route("/", methods=["POST"])
def webhook():
    data = request.json
    if "message" in data and "document" in data["message"]:
        file_id = data["message"]["document"]["file_id"]
        file_info = requests.get(f"https://api.telegram.org/bot{TOKEN}/getFile?file_id={file_id}").json()
        file_path = file_info['result']['file_path']
        download_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
        print("Download URL:", download_url)
    return "OK"

@app.route("/", methods=["GET"])
def home():
    return "Bot is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
