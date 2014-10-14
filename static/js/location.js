$(document).ready(function () {
    if ("geolocation" in navigator) {
        console.log("Geolocation Available!");
        navigator.geolocation.getCurrentPosition(function (pos) {
            console.log("lat: " + pos.coords.latitude);
            console.log("lng: " + pos.coords.longitude);
            console.log(pos);

            var reverse_payload = {
                latlng: pos.coords.latitude + "," + pos.coords.longitude,
                key: "AIzaSyDDOJStRQzhlys5a_ffsJMekYtaQYkDwLQ"
            };

            var reverse_url = "https://maps.googleapis.com/maps/api/geocode/json";

            $.get(reverse_url, reverse_payload, function (response) {
                console.log(response)
                var location_verbose = response.results[0].formatted_address;

                var location_payload = {
                    "id": 2,
                    "user": 2,
                    "lat": pos.coords.latitude.toString(),
                    "lng": pos.coords.longitude.toString(),
                    "verbose_loc": location_verbose
                };

                $.ajax({
                    url: "/api/user/location/2/",
                    type: "PUT",
                    data: location_payload,
                    success: function (response) {
                        console.log(response);
                    }
                })
            });


        })
    } else {
        console.log("Geolocation Unavailable!");
    }
})