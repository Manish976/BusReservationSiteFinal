var dp = null;
attachDatePicker = function(){
    if(dp === null || typeof dp === 'undefined')
        dp = TinyDatePicker('.test input');
}

$(function(){
    if($(this).width() <500){
           $('.datepicker').removeClass('test').addClass('red');
           $('#myinput').attr('type','date');
            //you should alsa remove TinyDatePicker here
            if(dp !== null){
                dp.destroy();
                dp = null;
            }
        }
        else{
            $('div').removeClass('red').addClass('test');
           $('#myinput').attr('type','text');
            attachDatePicker();
        }
});

jQuery(document).ready(function(){
  attachDatePicker();
});