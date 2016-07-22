from flask import Flask
from flask import render_template
import time #simulating slow calculation

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/fetch')
def fetch_recipe():
    time.sleep(3)
    return "Test"


if __name__ == "__main__":
    app.run()
