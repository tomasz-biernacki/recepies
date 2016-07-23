from flask import Flask
from flask import render_template, jsonify
from random import randint
import time #simulating slow calculation

app = Flask(__name__)

def read_rand_file():
    r = randint(1, 50)
    file_name = "sample_" + str(r)
    print "READING " + file_name
    content = ""
    with open('samples/' + file_name, 'r') as content_file:
        content = content_file.read()
    return content

def modify_output_recipie(nn_output):
    descriptions = []
    ingredients = []
    splitted = nn_output.split('\n')
    ing = False
    steps = False
    for l in splitted:
        if l == "" or l == "\n:":
            continue
        if l == "<!SKLADNIKI>:":
            ing = True
            continue
        if l == "<!PRZEPIS>":
            ing = False
            steps = True
            continue
        if l == "<!STOP>":
            break
        if ing == True:
            ingredients.append(l)
        if steps == True:
            descriptions.append(l)

    return jsonify(ingredients=ingredients,
                   descriptions=descriptions)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/fetch')
def fetch_recipe():
    time.sleep(1)
    try:
        return modify_output_recipie(read_rand_file())
    except Exception as e:
        return jsonify(error=str(e))

if __name__ == "__main__":
    app.run()
