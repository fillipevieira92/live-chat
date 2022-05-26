function redirect (room_id) {
    var user_id = document.querySelector('#user_id').value;
    var username = document.querySelector('#username').value;
    data = {
        'room_id':room_id,
        'user_id':user_id,
        'username':username,
    }
    $.ajax({
        url: '/chat',
        data: {'data':JSON.stringify(data)},
        dataType: 'json',
        success:function(){
            window.location.href = '/chat'
        }
    })
}