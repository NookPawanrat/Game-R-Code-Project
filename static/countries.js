let map = L.map('map').setView([0, 0], 2);
const countries = [{"nombre": "Reino Unido", "lat": 51.509865, "long": -0.118092},
         {"nombre": "Argentina", "lat": -34.611778, "long": -58.417309},
         {"nombre": "Tailand", "lat": 13.756331, "long": 100.501765},
         {"nombre": "Egipt", "lat": 30.033, "long": 31.233},
         {"nombre": "Australia", "lat": -25.274398, "long": 133.775136},
         {"nombre": "Brasil", "lat": -14.235004, "long": -51.92528},
         {"nombre": "China", "lat": 35.86166, "long": 104.195397}];

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

let ricina_icon = L.icon({
    iconUrl: '../static/images/ricina icon.webp', // Replace with the URL of your custom marker image
    iconSize: [15, 15], // Set the size of the custom marker image
    popupAnchor: [0, -10] // Set the popup anchor point relative to the iconAnchor
  });

for(c of countries){
    let marker = L.marker([c.lat, c.long], { icon: ricina_icon }).addTo(map);
    marker.bindPopup(c.nombre).openPopup();
}
