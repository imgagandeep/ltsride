
// Set map options
var lat_long = {lat: 31.4330719, lng: 75.2814839};
var mapOptions = {
    center: lat_long,
    zoom: 5,
    mapTypeId: google.maps.MapTypeId.ROADMAP

};

// Create map
var map = new google.maps.Map(document.getElementById('google_map'), mapOptions);

// Create a DirectionsService object to use the route method and get a result for our request
var directionsService = new google.maps.DirectionsService();

// Create a DirectionsRenderer object which we will use to display the route
var directionsDisplay = new google.maps.DirectionsRenderer();

// Bind the DirectionsRenderer to the map
directionsDisplay.setMap(map);


// Define calcRoute function
function calcRoute() {
    // Create request
    var request = {
        origin: document.getElementById("source").value,
        destination: document.getElementById("destination").value,
        travelMode: google.maps.TravelMode.DRIVING, //WALKING, BYCYCLING, TRANSIT
        unitSystem: google.maps.UnitSystem.IMPERIAL
    }

    // Pass the request to the route method
    directionsService.route(request, function (result, status) {
        if (status == google.maps.DirectionsStatus.OK) {
            // Get distance and time
            // const output = document.querySelector('#output');
            const distance = document.querySelector('#distance');
            // output.innerHTML = "<div>Source: " + document.getElementById("source").value + "<br/>Destination: " + document.getElementById("destination").value + "<br/> Driving Distance: " + result.routes[0].legs[0].distance.text + "<br/>Duration: " + result.routes[0].legs[0].duration.text + "</div>";
            distance.value = result.routes[0].legs[0].distance.text
            // Display route
            directionsDisplay.setDirections(result);
        }
        else {
            // Delete route from map
            directionsDisplay.setDirections({ routes: [] });
            // Center map in London
            map.setCenter(lat_long);
            // Show error message
            // output.innerHTML = "<div>Could not retrieve driving distance.</div>";
        }
    });

}



// Create autocomplete objects for all inputs
var options = {
    types: ['(cities)']
}

var address_a = document.getElementById("source");
var autocomplete1 = new google.maps.places.Autocomplete(address_a, options);

var address_b = document.getElementById("destination");
var autocomplete2 = new google.maps.places.Autocomplete(address_b, options);

