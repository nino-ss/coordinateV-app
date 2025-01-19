from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# 天気に応じたコーディネート候補
weather_coordinates = {
    'sunny': ['白Tシャツ×デニム', 'ワンピース', 'ポロシャツ×チノパン'],
    'rainy': ['レインコート×デニム', '撥水パンツ×長袖シャツ', 'ワンピース×カーディガン'],
    'cloudy': ['パーカー×スラックス', 'ニット×スカート', 'シャツ×デニム']
}

# TPOに応じたコーディネート候補
tpo_coordinates = {
    'casual': ['Tシャツ×デニム', 'パーカー×スウェット', 'カットソー×チノパン'],
    'business': ['スーツ', 'ブラウス×スカート', 'シャツ×スラックス'],
    'party': ['ドレス', 'ジャケット×パンツ', 'ブラウス×スカート']
}

# 気分に応じたコーディネート候補
mood_coordinates = {
    'happy': ['カラフルワンピース', '明るい色のTシャツ×デニム', 'プリントTシャツ×スカート'],
    'relaxed': ['ゆったりニット×パンツ', 'スウェット上下', 'ワイドパンツ×カットソー'],
    'cool': ['黒シャツ×スキニー', 'レザージャケット×デニム', 'モノトーンコーデ']
}

@app.route('/')
def index():
    print("Rendering index page")
    return render_template('index.html')

@app.route('/get_coordinate', methods=['POST'])
def get_coordinate():
    print("Received coordinate request")
    data = request.get_json()
    weather = data.get('weather', 'sunny')
    tpo = data.get('tpo', 'casual')
    mood = data.get('mood', 'happy')
    
    # それぞれの条件に合うコーディネートをランダムに選択
    weather_coord = random.choice(weather_coordinates[weather])
    tpo_coord = random.choice(tpo_coordinates[tpo])
    mood_coord = random.choice(mood_coordinates[mood])
    
    # 3つの候補から最終的な1つを選択
    final_coordinate = random.choice([weather_coord, tpo_coord, mood_coord])
    
    return jsonify({
        'coordinate': final_coordinate,
        'message': 'あなたにおすすめのコーディネートです！'
    })

if __name__ == '__main__':
    print("Starting Coordinate Application...")
    print("Please access: http://127.0.0.1:5000")
    app.run(debug=True, port=5000)