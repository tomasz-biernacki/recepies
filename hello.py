from flask import Flask
from flask import render_template, jsonify
import time #simulating slow calculation

app = Flask(__name__)

fake_ingredients = ["100g kurczaka", "200g papryk", "50g piwa"]
fake_descriptions = ["Place the zucchini, bell pepper, and pineapple in a mixing bowl. Drizzle with olive oil, and toss to coat. Divide the mixture into freezer bags. Whisk the ketchup, salt, steak sauce, sugar, vinegar, Worcestershire sauce, and water together in the same bowl until smooth. Add the beef cubes, and toss until evenly coated. Divide the beef into freezer bags. Seal, and freeze the bags.", "Place the zucchini, bell pepper, and pineapple in a mixing bowl. Drizzle with olive oil, and toss to coat. Divide the mixture into freezer bags. Whisk the ketchup, salt, steak sauce, sugar, vinegar, Worcestershire sauce, and water together in the same bowl until smooth. Add the beef cubes, and toss until evenly coated. Divide the beef into freezer bags. Seal, and freeze the bags."]

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/fetch')
def fetch_recipe():
    time.sleep(1)
    return jsonify(ingredients=fake_ingredients,
                   descriptions=fake_descriptions)

if __name__ == "__main__":
    app.run()
