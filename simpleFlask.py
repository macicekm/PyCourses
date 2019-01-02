
#https://codeburst.io/flask-for-dummies-a-beginners-guide-to-flask-part-uno-53aec6afc5b1

#https://aryaboudaie.com/python/technical/educational/web/flask/2018/10/17/flask.html
from flask import Flask

app = Flask(__name__) #app is the name of the object here


@app.route('/')
def home():
    return "<h1> Hello World ! </h1>"


if __name__ == "__main__":
    app.run(debug=True, port=8080)

