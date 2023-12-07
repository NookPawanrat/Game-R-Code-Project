var map = L.map('map').setView([0, 0], 2);

let ricina_icon = L.icon({
    iconUrl: '../static/images/ricina icon.webp',
    iconSize: [50, 30],
    popupAnchor: [0, -10]
});

for(c of countries){
    let marker = L.marker([c["lat"], c["long"]], { icon: ricina_icon }).addTo(map);
    marker.bindPopup(c['country']).openPopup();
}

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors'
}).addTo(map);