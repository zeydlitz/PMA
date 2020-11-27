function map_init_basic(map, options) {
L.marker([50.5, 30.5]).addTo(map);
                               {% for e in object_list %}

                                    L.marker({{e}}).addTo(map);
                                {% endfor %}
    // var mymap = L.map(map).setView([55, 26], 5);
    // L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    //     attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    //     maxZoom: 18,
    //     id: 'mapbox/streets-v11',
    //     tileSize: 512,
    //     zoomOffset: -1,
    // }).addTo(map);

}