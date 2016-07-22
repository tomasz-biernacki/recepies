var loadingDiv = document.getElementById('loading');
var outputDiv = document.getElementById('output');

function fetch_data () {
  loadingDiv.style.display = 'block';
  output.innerHTML = "";

  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (xhttp.readyState == 4 && xhttp.status == 200) {
      loadingDiv.style.display = 'none';
      output.innerHTML = xhttp.responseText;
    }
  };
  xhttp.open("GET", "/fetch", true);
  xhttp.send();
}
