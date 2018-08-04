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
});