from flask import Flask
from flask import render_template
from flask import redirect
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Flask!"

@app.route('/add/num1=<num1>&num2=<num2>', methods=['GET'])
def add(num1,num2):
    print(num1 + num2, type(num1))
    return str(int(num1) + int(num2))

@app.route('/add/num1=<int:num1>&&num2=<int:num2>', methods=['GET'])
def add2(num1,num2):
    print(num1 + num2, type(num1))
    return str(num1+num2)

@app.route("/index")
def index():
    return render_template(r"01.html")

@app.route("/goto/<path:url>", methods=['GET'])
def _goto(url):
    print('redirect:', url)
    return redirect(url)

@app.route("/css")
def css():
    return render_template(r"css.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)