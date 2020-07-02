// Call the dataTables jQuery plugin
$(document).ready(function() {
  $('#dataTable').DataTable();
  $('#tableInt').DataTable( {
        "paging":   false,
        "ordering": true,
        "searching":     false,
		"lengthChange": false,
		"info": false
    } );
});
