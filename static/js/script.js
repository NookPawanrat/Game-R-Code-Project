'use strict'

document.addEventListener("DOMContentLoaded", function(){
  fetch('/get_data')
        .then(response => response.json())
        .then(data => {
          const fulllife = data.full_life;
          const lifeleft = data.left_life;
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
          document.querySelector('.player_name').innerText = data.player_name;
          document.querySelector('.player_id').innerText = data.player_id;
          document.querySelector('.numbers-to-win').innerText = data.mission_left;
          document.querySelector('.mission_left').innerText = data.mission_left;
          document.querySelector('.left_life').innerText = data.left_life;
          const locationelements = document.querySelectorAll('.player_location');
          for (let l of locationelements) {
            l.innerText = data.player_location;
          }
        })
        .catch(error => console.error('Error:', error));
})

