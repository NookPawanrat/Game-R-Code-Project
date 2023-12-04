document.getElementById('showcountries').addEventListener('click', function(){
  window.open("http://127.0.0.1:5000/countries");
})

document.getElementById('howtoplay').addEventListener('click', function(){
  window.location.href = 'http://127.0.0.1:5000/howto';
})

document.getElementById('exit').addEventListener('click', function(){
  window.location.href = 'http://127.0.0.1:5000/exit';
})