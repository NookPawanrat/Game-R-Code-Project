function init_map(countries){
    let map = L.map('map').setView([0, 0], 2);

    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 10}).addTo(map);

    let ricina_icon = L.icon({
        iconUrl: '../static/images/ricina icon.webp',
        iconSize: [50, 30],
        popupAnchor: [0, -10]
      });

    let dropped_icon = L.icon({
        iconUrl: '../static/images/killicon.webp',
        iconSize: [50, 30],
        popupAnchor: [0, -10]
      });

    for(c of countries){
        let marker = L.marker([c["lat"], c["long"]], { icon: ricina_icon }).addTo(map);
        marker.bindPopup(c['country']).openPopup();
    }
}