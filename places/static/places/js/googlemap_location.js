/*
 * A simple Google maps Javascript widget which will display a map and
 * a marker with the ability to move the marker, then setting the
 * lat/lng of the marker into the specified (or default) fields.
 */

var google_map_location = new function() {
    var jQuery;
    var init_options;
    var geocoder;

    var map, marker, latlng;


    /*
     * Options available:
     *  zoom: zoom level of map (default: 14)
     *  lat: initial lat of map
     *  lng: initial lng of map
     *  markerMovedCallback: callback function to use when marker is moved to populate a lat field.
     */
    this.init = function(options) {
        // Work around for when we have to use closures through django admin to pass in the jQuery object.
        jQuery = options.jQuery || $;
        init_options = options;

        latlng = new google.maps.LatLng(
                options.lat || 14.0723,
                options.lng || -87.1921
        );

        var myOptions = {
            zoom: options.zoom || 14,
            center: latlng,
            mapTypeId: google.maps.MapTypeId.ROADMAP
        };

        map = new google.maps.Map(document.getElementById('map_canvas'),
                            myOptions);

        marker = new google.maps.Marker({
                    position: latlng,
                    map: map,
                    draggable: true,
                    animation: google.maps.Animation.DROP
        });

        this.bindHandlers();

        // Attempt to get an initialLocation.
        if (options.geolocate && navigator.geolocation) {
            browserSupportFlag = true;
            navigator.geolocation.getCurrentPosition(this.hasPosition, this.noPosition);
        }
    }

    // Once we have received a poistion, center our map and marker to it.
    this.hasPosition = function(position) {
        latlng = new google.maps.LatLng(position.coords.latitude,
                        position.coords.longitude);

        map.setCenter(latlng);
        marker.setPosition(latlng)

    }

    // If we have nothing, just show a friendly message
    this.noPosition = function(error) {
        jQuery("#map_message").html("Could not get current location. Please place marker over the Places location.");
    }

    /*
     * Accept an input field that contains a val() object from jQuery and tries to encode
     * an address from it.
     */
    this.codeAddress = function(field) {
        var self = this;
        geocoder = new google.maps.Geocoder();

        geocoder.geocode({'address': field.val()}, function(results, status) {
            map.setCenter(results[0].geometry.location);
            marker.setPosition(results[0].geometry.location);
            self.populateLatLngFields(results[0].geometry.location);
        });

    }

    this.populateLatLngFields = function(point) {
        jQuery("#id_latitude").val(point.lat());
        jQuery("#id_longitude").val(point.lng());
    };

    this.bindHandlers = function() {
        var self = this;

        google.maps.event.addListener(marker, 'dragend', function() {
            var point = marker.getPosition();

            if(init_options.markerMovedCallback) {
                init_options.markerMovedCallback(point);
            } else {
                self.populateLatLngFields(point);
            }
        });

        // double click event
          google.maps.event.addListener(map, 'dblclick', function(e) {
            var positionDoubleclick = e.latLng;
            marker.setPosition(positionDoubleclick);

            if(init_options.markerMovedCallback) {
                init_options.markerMovedCallback(positionDoubleclick);
            } else {
                self.populateLatLngFields(positionDoubleclick);
            }

            // if you don't do this, the map will zoom in
            e.stopPropagation();
          });
    };


};