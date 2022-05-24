$('#username').on('keyup', function(){
    if (this.value.length >= 5) {
        $('.button').removeClass('disabled').prop('disabled', false);
        $('#alerta-caracteres').prop('hidden', true);
    } else {
        $('.button').addClass('disabled').prop('disabled', true);
        $('#alerta-caracteres').prop('hidden', false);
    }
});