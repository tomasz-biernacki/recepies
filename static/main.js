var loadingDiv = document.getElementById('loading');
var outputDiv = document.getElementById('output');
var ingredientsDiv = document.getElementById('ingredients');
var descriptionDiv = document.getElementById('description');

function build_ingredients(ingredients) {
  ingredientsDiv.innerHTML = "";
  ingredients.forEach(function(item, index) {
    ingredientsDiv.innerHTML += "<div class='ingredients-item'>" + item + "</div>";
  });
}

function build_description(descriptions) {
  descriptionDiv.innerHTML = "";
  var many = descriptions.length > 1;

  descriptions.forEach(function(item, index) {
    if(many) {
      descriptionDiv.innerHTML += "<div class='description-index'>" + (index+1) + "</div>";
    }
    descriptionDiv.innerHTML += "<div class='description-item'>" + item + "</div>";
  })
}

function build_recipe (data) {
  var ingredients = data['ingredients'];
  build_ingredients(ingredients);
  var descriptions = data['descriptions'];
  build_description(descriptions);
}

function fetch_data () {
  outputDiv.style.display = 'none';
  loadingDiv.style.display = 'block';

  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (xhttp.readyState == 4 && xhttp.status == 200) {
      loadingDiv.style.display = 'none';
      outputDiv.style.display = 'block';
      if(xhttp.responseText.error)
        alert(xhttp.responseText.error)
      else
        build_recipe(JSON.parse(xhttp.responseText));
    }
  };
  xhttp.open("GET", "/fetch", true);
  xhttp.send();
}
