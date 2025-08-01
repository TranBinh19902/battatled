from flask import Flask, render_template, request, jsonify
import requests

ESP32_IP = "http://<ESP32-IP>:80"  # <-- Thay bằng IP thực tế ESP32

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/set-effect/<int:effect_id>', methods=['POST'])
def set_effect(effect_id):
    try:
        res = requests.get(f"{ESP32_IP}/set?effect={effect_id}", timeout=2)
        return jsonify({'status': 'ok', 'esp_response': res.text})
    except:
        return jsonify({'status': 'error', 'message': 'ESP32 không phản hồi'}), 500

if __name__ == '__main__':
    app.run(debug=True)
