import random
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('hello.html')

@app.route('/hi')
def hi():
    return render_template('hi.html')

# variable routing! 경로를 변수로 활용한다.
@app.route('/hi/<string:name>')
def higyo(name):
    # return f'<h1>{name}아 안녕!!!</h1>'
    return render_template('hi2.html', name=name)

# /cube/<숫자>
# 세제곱 결과를 보여주는 페이지!
@app.route('/cube/<int:number>')
def cube(number):
    return f'{number} 의 세제곱은 {number**3} 이다.'

# /lunch/사람이름
# 한식, 스페셜A, 스페셜B
@app.route('/lunch/<string:name>')
def lunch(name):
    menu = ['한식', '스페셜A', '스페셜B']
    return render_template('lunch.html',name=name, menu=random.choice(menu))

# 로또!
# /lotto
# 로또 번호 6개를 추천해주는 페이지
@app.route('/lotto')
def lotto():
    ls = random.sample(range(1,46), 6)
    a = str(sorted(ls))
    return f'이번주 당첨번호는 {a} !!'
    
if __name__ == '__main__':
    # python app.py 를 하면 아래의 코드 블록을 실행시킨다.
    app.run(debug=True)