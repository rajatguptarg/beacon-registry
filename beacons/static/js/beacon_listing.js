(function beaconsList(){
      var columnWidths = [
          null,
          {orderable : false, targets :0},
          null,
          null,
          {orderable : false, targets :0},
          {orderable : false, targets :0},
          {orderable : false, targets :0},
          {orderable : false, targets :0}
      ];
    $(document).ready(function(){
        beaconsList.init();
    });

    beaconsList.init = function(){
        $('#beaconsTable').dataTable(
             {
                "columns":columnWidths,
                "order": [[ 1, "asc" ]],
                "language": {
                    "zeroRecords": "No beacons to show",
                    "info": "Showing page _PAGE_ of _PAGES_",
                    "infoEmpty": "No beacons available",
                    "infoFiltered": "(filtered from _MAX_ total records)"
                },
                "lengthMenu": [[5, 10, 20, 50, -1], [5, 10, 20, 50, "All"]]
             }
        );
    }
})();
