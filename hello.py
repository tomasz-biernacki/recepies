from flask import Flask
from flask import render_template, jsonify
import time #simulating slow calculation
import subprocess

app = Flask(__name__)

fake_ingredients = ["100g kurczaka", "200g papryk", "50g piwa","100g kurczaka", "200g papryk", "50g piwa","100g kurczaka", "200g papryk", "50g piwa"]
fake_descriptions = ["Place the zucchini, bell pepper, and pineapple in a mixing bowl. Drizzle with olive oil, and toss to coat. Divide the mixture into freezer bags. Whisk the ketchup, salt, steak sauce, sugar, vinegar, Worcestershire sauce, and water together in the same bowl until smooth. Add the beef cubes, and toss until evenly coated. Divide the beef into freezer bags. Seal, and freeze the bags.", "Place the zucchini, bell pepper, and pineapple in a mixing bowl. Drizzle with olive oil, and toss to coat. Divide the mixture into freezer bags. Whisk the ketchup, salt, steak sauce, sugar, vinegar, Worcestershire sauce, and water together in the same bowl until smooth. Add the beef cubes, and toss until evenly coated. Divide the beef into freezer bags. Seal, and freeze the bags."]

description = []
ingredients = []

def modify_output_recipie(nn_output):
    recipie = nn_output.split('\n',2)[2]
    recipie = recipie.split('<!PRZEPIS>')
    raw_ingredients = recipie[0].split(',')
    raw_description = recipie[1]
    description.append(raw_description)
    ingredients.extend(raw_ingredients)
    
def run_recipe_generator():
    bashCommand = "bash command"
    output = subprocess.check_output(['bash','-c', bashCommand])
    modify_output_recipie(output)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/fetch')
def fetch_recipe():
    time.sleep(1)
    run_recipe_generator()
    return jsonify(ingredients=ingredients,
                   descriptions=description)


if __name__ == "__main__":
    app.run(host="206.252.196.66",port=5000)
