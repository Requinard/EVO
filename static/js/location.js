$(document).ready(function () {
    if ("geolocation" in navigator) {
        console.log("Geolocation Available!");
        navigator.geolocation.getCurrentPosition(function (pos) {
            console.log("lat: " + pos.coords.latitude);
            console.log("lng: " + pos.coords.longitude);
            console.log(pos);
            var reverse_payload = {
                lat: pos.coords.latitude,
                lng: pos.coords.longitude,
                username: "demo"
            }

            var reverse_url = "http://api.geonames.org/findNearbyJSON"

            $.get(reverse_url, reverse_payload, function(response){
                console.log(response)
            })

        })
    } else {
        console.log("Geolocation Unavailable!");
    }
})