// Call the dataTables jQuery plugin
$(document).ready(function() {
  $('#dataTable').DataTable();
  $('#dataTable1').DataTable();
  $('#dataTable2').DataTable();
  $('#dataTable3').DataTable();
  $('#dataTable4').DataTable();
  $('#tableInt').DataTable( {
        "paging":   false,
        "ordering": true,
        "searching":     false,
		"lengthChange": false,
		"info": false
    } );
});
