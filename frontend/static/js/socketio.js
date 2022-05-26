$(document).ready(function(){
    var socket = io('/chat');
    
    const username = document.querySelector('#username').value;
    const user_id = document.querySelector('#user_id').value;
    const room_id = document.querySelector('#room_id').value;
    

    socket.on('connect', function() {
        data = {
            msg:'Conectado ao socket',
            username:username,
            user_id:user_id,
            user_session:socket.id,
            room_id:room_id
        }
        socket.emit('connect_event', data);
        
    });
    socket.on('teste', conectando(socket, username, String(new Date().getHours()+':'+new Date().getMinutes())))
    socket.on('disconnect', function(){
        data = {
            msg:'Desconectado do socket',
            username:username,
            user_id:user_id,
            user_session:socket.id,
            room_id:room_id
        }
        socket.emit('disconnect_event', data);
    })


    
})

function conectando (socket, username, hora) {
    msg = `${username} acabou de entrar na sala. ${hora} `
    socket.send(alert(msg))
}




