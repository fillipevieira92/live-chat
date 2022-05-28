$('#username').on('keyup', function(){
    if (this.value.length >= 5) {
        $('#alerta-caracteres').prop('hidden', true);
        $.ajax({
            url:'ajax',
            data:{'username':JSON.stringify(this.value)},
            dataType:'json',
            success:function(data){
                if (data.response == 'ok') {
                    $('.button').removeClass('disabled').prop('disabled', false);
                    $('#alerta-usuario-existente').prop('hidden', true);
                } else {
                    $('#alerta-usuario-existente').prop('hidden', false);
                    $('.button').addClass('disabled').prop('disabled', true);
                }
            }
        })
        
    } else {
        $('.button').addClass('disabled').prop('disabled', true);
        $('#alerta-caracteres').prop('hidden', false);
        $('#alerta-usuario-existente').prop('hidden', true)
    }
});
