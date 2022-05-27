function logout() {
    let user_id = document.querySelector('#user_id')
    let room_id = document.querySelector('#room_id')
    let username = document.querySelector('#username')
    let data = {
        'user_id':user_id.value,
        'room_id':room_id.value,
        'username':username.value
    }

    $.ajax({
        url:'/logout',
        data: {'data':JSON.stringify(data)},
        dataType:'json',
        success:function(){
            window.location.href = '/'
        }
    })



}