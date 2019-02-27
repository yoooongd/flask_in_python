import random
import requests

from faker import Faker

#flask를 사용할 거야
from flask import Flask,render_template
app = Flask(__name__)


#
@app.route("/")
def hello():
    return "Hello World!"

@app.route("/multi_c")
def greeting():
    return "멀캠c반!"
    
    
@app.route("/html_tag")
def html_tag():
    return """
    <h1>HTML태그도 보낼 수 있어요</h1>
    <p>안녕하세요</p>
    """

@app.route("/html_file")
def html_file():
    return render_template("html.html")

@app.route("/hi/<string:name>")
def hi(name):
    return render_template("hi.html",name=name)

@app.route("/cube/<int:num>")
def cube(num):
    cubic = num ** 3 #**은 제곱을 의미
    return render_template("cube.html", num=num, cubic=cubic)

@app.route("/dinner")
def dinner():
    menu_list = ["김밥까페","시골집","강남목장","양자강"]
    pick = random.choice(menu_list)
    return render_template("dinner.html",pick=pick)

@app.route("/lotto")
def lotto():
    numbers = range(1,46)
    pick = random.sample(numbers,6)
    return render_template("lotto.html",pick=pick)

@app.route("/random_img")
def random_img():
    return render_template("random_img.html")
    
    
@app.route("/ego/<string:name>")
def ego(name):
    url="http://api.giphy.com/v1/gifs/search?api_key=pG4yTEG1AxRiWdSXqj3Cjd8vsDmnkV2E&q="
    fake = Faker("ko_KR")
    job = fake.job()
    
    res=requests.get(url+job).json()
    img_url=res["data"][0]["images"]["original"]["url"]
    
    return render_template("ego.html",img_url=img_url,name=name,job=job)


#서버 실행 옵션    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=8080)