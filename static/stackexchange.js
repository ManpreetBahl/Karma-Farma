/*
Copyright 2018 Manpreet Bahl
[This program is licensed under the "MIT License"]
Please see the file LICENSE in the source distribution 
of this software for license terms.
*/

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