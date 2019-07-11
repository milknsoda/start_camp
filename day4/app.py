# 0. flask 패키지 가져오기
from flask import Flask, render_template, request
import random

# 1. app 설정
app = Flask(__name__)

# 2. 요청 경로(route) + 함수 만들기
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/<string:name>')
def hello(name):
    return render_template('hello.html', name=name)

@app.route('/lunch')
def lunch():
    menus = ['레드코코넛누들', '소불고기', '삼계탕', '싸이버거', '치킨']
    pick  = random.choice(menus)
    return render_template('lunch.html', menus=menus, pick=pick)

@app.route('/naver')
def naver():
    return render_template('naver.html')

@app.route('/ping')
def pingpong():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    # 사용자가 보낸 데이터를 받아와서
    text = request.args.get('say')
    # 템플릿에 넘겨준다. 
    return render_template('pong.html', text=text)

@app.route('/vonvon')
def vonvon():
    return render_template('vonvon.html')

@app.route('/von_result')
def von_result():
    fit = ['인성', '천재성', '백치미', '미모', '경제력', '키']
    string = ['도 조금 넣고', '은(는) 적당히..', '은(는) 필요없겠네', '...', '은(는) 조금만...우아ㅏ아ㅏㅏ악']
    name = request.args.get('name')
    return render_template('/von_result.html', name=name, fit=random.sample(fit, 3), string=random.sample(string, 3))

@app.route('/random_game')
def random_game():
    return render_template('random.html')

@app.route('/result')
def result():
    mood = request.args.get('mood')
    weather = request.args.get('weather')
    return render_template('result.html', mood=mood, weather=weather)

if __name__ == '__main__':
    app.run(debug=True)
