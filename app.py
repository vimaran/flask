from flask import Flask,render_template,url_for

from datetime import datetime

app = Flask(__name__)


@app.route('/')
def basic():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')
if __name__ =='__main__':
    app.run()
