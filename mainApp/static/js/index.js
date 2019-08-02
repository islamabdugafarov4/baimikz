let map;
function initMap() {
    let latlng = {lat: 51.130382, lng: 71.514124};

    map = new google.maps.Map(document.getElementById('map'), {
        zoom: 17,
        center: latlng
    });

    let marker = new google.maps.Marker({
        position: latlng,
        map: map,
        title: 'Мы здесь!!!'
    });

}

