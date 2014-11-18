$("#action-update-location").click(function (e) {
    e.preventDefault();
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
                    "id": user_location_id,
                    "user": user_id,
                    "lat": pos.coords.latitude.toString(),
                    "lng": pos.coords.longitude.toString(),
                    "verbose_loc": location_verbose
                };

                $.ajax({
                    url: "/api/user/location/" + user_location_id + "/",
                    type: "PUT",
                    data: location_payload,
                    success: function (response) {
                        console.log(response);
                        console.log("Succesfully PUT location data.")


                    }
                })
                $("#response-location-updated").addClass("bg-info");
                $("#action-update-location").text("Updated!");
            });


        })
    } else {
        console.log("Geolocation Unavailable!");
    }
});