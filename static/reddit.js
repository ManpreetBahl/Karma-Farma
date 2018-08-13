/*
Copyright 2018 Manpreet Bahl
[This program is licensed under the "MIT License"]
Please see the file LICENSE in the source distribution 
of this software for license terms.
*/
jQuery(document).ready(function () {
    if(jQuery('#redditTable').length > 0){
        jQuery('#redditTable').DataTable();
        jQuery('#redditTable').show();
    }
});