(function beaconsList(){
    $(document).ready(function(){
        beaconsList.init();
    });

    beaconsList.init = function(){
        $('#beaconsTable').dataTable();
    }
})();
