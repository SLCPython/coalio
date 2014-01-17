'use strict';
$(function () {
    $('.helpText').hide();
    $('#helpSelection').change(function () {
        var helpSelection = $('#helpSelection').val();
        $('.helpText').hide();
        if(helpSelection == '1'){
            $('#bullyingContent1').show();
        } else if (helpSelection == '2') {
            $('#bullyingContent2').show();
        }
        else {
            $('#bullyingContent3').show();
        }
    });
});