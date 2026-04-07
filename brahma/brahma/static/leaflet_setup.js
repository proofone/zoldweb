function initLeafletMap() {

    var map = L.map("map-container").setView([47.083, 19.528], 7);
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);
}

if (document.readyState === "loading") {
    // Loading hasn't finished yet
    document.addEventListener("DOMContentLoaded", initLeafletMap);
  } else {
    // `DOMContentLoaded` has already fired
    initLeafletMap();
  }
