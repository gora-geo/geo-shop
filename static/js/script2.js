$(document).ready(function(){
    $('#zac').hide();
     $('#name').hide();
     $('#phone').hide();

    $('#oformit').on('click',function() {
        $(this).hide();
        $('#zac').show();
        $('#name').show();
        $('#phone').show();
        $('#table').hide();

    });

});
