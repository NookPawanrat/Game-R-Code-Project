'use strict'

document.addEventListener("DOMContentLoaded", function(){
  fetch('/get_data')
        .then(response => response.json())
        .then(data => {
          console.log(data);
          const fulllife = data.full_life;
          const lifeleft = data.left_life;
          const ricinas = document.querySelectorAll('img.ricina-img');
          if (lifeleft < fulllife){
            for (let i = 0; i<fulllife-lifeleft; i++) {
            ricinas[i].src = "../static/images/killicon.webp";
            }
          }
        })
        .catch(error => console.error('Error:', error));
})
