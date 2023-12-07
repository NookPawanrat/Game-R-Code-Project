'use strict'

document.addEventListener("DOMContentLoaded", function(){
  fetch('/get_data')
        .then(response => response.json())
        .then(data => {
          console.log(data)
          const fulllife = data.full;
          const lifeleft = data.left;
          const target = document.querySelector('.ricina-images');
          target.innerHTML = '';
          for (let i = 0; i<fulllife-lifeleft; i++) {
            const fail = document.createElement('img');
            fail.className = 'ricina-img';
            fail.src = '../static/images/killicon.webp';
            target.appendChild(fail)
            }
          for (let i = 0; i< lifeleft; i++ ) {
            const life = document.createElement('img');
            life.className = 'ricina-img';
            life.src = '../static/images/ricina%20fill.png';
            target.appendChild(life);
            }
        })
        .catch(error => console.error('Error:', error));
})

