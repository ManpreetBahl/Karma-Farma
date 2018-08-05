function format ( d ) {
    return  'The child row can contain any data you wish, including links, images, inner tables etc.';
}

jQuery(document).ready(function () {
    if(jQuery('#bestTable').length > 0){
        jQuery('#bestTable').DataTable();
        jQuery('#bestTable').show();
    }

    if(jQuery('#goodTable').length > 0){
        jQuery('#goodTable').DataTable();
        jQuery('#goodTable').show();
    }

    if(jQuery('#okayTable').length > 0){
        jQuery('#okayTable').DataTable();
        jQuery('#okayTable').show();
    }

    $('#goodTable tbody').on('click', 'tr td.details-control', function () {
        var tr = $(this).closest('tr');
        var row = table.row( tr );
 
        if ( row.child.isShown() ) {
            // This row is already open - close it
            row.child.hide();
            tr.removeClass('shown');
        }
        else {
            // Open this row
            row.child( format(row.data()) ).show();
            tr.addClass('shown');
        }
    } );
});