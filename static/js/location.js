$("#action-update-location").click(function (e) {
    e.preventDefault();

    // Get User data
    var userID = getUserId();
    var csrf_token = getCookie("csrftoken");


    // Check if we can see location
    if ("geolocation" in navigator) {

        // Poll for current position
        navigator.geolocation.getCurrentPosition(function (pos) {

            // Create a payload to get an estimated address from google
            var reverse_payload = {
                latlng: pos.coords.latitude + "," + pos.coords.longitude,
                key: "AIzaSyDDOJStRQzhlys5a_ffsJMekYtaQYkDwLQ"
            };

            // Google's geocoding API
            var reverse_url = "https://maps.googleapis.com/maps/api/geocode/json";

            // Ask google nicely if we can have an address
            $.get(reverse_url, reverse_payload, function (response) {

                // Save our verbose location
                var location_verbose = response.results[0].formatted_address;

                // Prepare our location payload to report to the API
                var location_payload = {
                    "id": +userID,
                    "user":+userID,
                    "lat": pos.coords.latitude,
                    "lng": pos.coords.longitude,
                    "verbose_loc": location_verbose
                };

                if (location_payload.verbose_loc === "")
                    location_payload.verbose_loc = "Unknown";


                // Add CSRF header to our AJAX request
                $.ajaxSetup({
                    headers: { "X-CSRFToken":csrf_token }
                });

                // Send our data payload to the API
                $.ajax({
                    url: "/api/user/location/" + userID + "/",
                    type: "PUT",
                    data: location_payload,
                    success: function (response) {
                        $("#response-location-updated").addClass("bg-info");
                        $("#action-update-location").text("Updated!");
                    },
                    error: function(response){
                        alert(response);
                        console.log(response);
                    }
                })
            });


        })
    } else {
        console.log("Geolocation Unavailable!");
    }
});