from flask import Flask
from flask import render_template, jsonify
import time #simulating slow calculation
import subprocess
from random import randint

app = Flask(__name__)

description = []
ingredients = []

def read_rand_file():
    r = randint(1, 50)
    r = 1 #uncomment
    file_name = "sample_" + str(r)
    content = ""
    with open('samples/' + file_name, 'r') as content_file:
        content = content_file.read()
    return content

def modify_output_recipie(nn_output):
    recipie = nn_output.split('\n',2)[2]
    recipie = recipie.split('<!PRZEPIS>')
    raw_ingredients = recipie[0].split(',')
    raw_description = recipie[1]
    description.append(raw_description)
    ingredients.extend(raw_ingredients)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/fetch')
def fetch_recipe():
    time.sleep(1)
    print read_rand_file()
    return jsonify(ingredients=ingredients,
                   descriptions=description)

if __name__ == "__main__":
    app.run()
