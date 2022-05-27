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

    socket.on('message', function(data){
        var chatMsg = document.querySelector('.chat-msg');
        var msgRow = document.createElement('div');

        /* var msg = document.createElement('div')
        var username = document.createElement('strong').setAttribute('class', 'msg-user')
        var msgBody = document.createElement('p').setAttribute('class', 'msg-body mb-0')
        var msgTime = document.createElement('p').setAttribute('class', 'msg-time float-end mb-0') */

        if (data.user_session != socket.id) {
            msgRow.innerHTML = `
            
                <div class="msg mb-1">
                    <strong class="msg-user">
                        ${data.username}
                    </strong>
                    <p class="msg-body mb-0">
                        ${data.msg}
                    </p>
                    <p class="msg-time float-end m-0">
                        ${data.time}
                    </p>
                </div>
            
            `
        } else {
            msgRow.innerHTML = `
            
                <div class="msg self-msg mb-1">
                    <strong class="msg-user">
                        ${data.username}
                    </strong>
                    <p class="msg-body mb-0">
                        ${data.msg}
                    </p>
                    <p class="msg-time float-end m-0">
                        ${data.time}
                    </p>
                </div>
            
            `
        }

        msgRow.setAttribute('class', 'msg-row');
        chatMsg.appendChild(msgRow);
        /* 
        $(username).text(data.username);
        $(msgBody).text(data.msg);
        $(msgTime).text(data.time);

        console.log(msgBody)
        console.log(msgRow)

        msg.appendChild(username,msgBody, msgTime);
        msgRow.appendChild(msg);
        chatMsg.appendChild(msgRow);
        */
        
    })

    /* 
    
    // Funçao .send para envio de mensagens

    time = String(new Date().getHours()+':'+new Date().getMinutes())

    data = {
        msg:msg,
        username:username,
        user_id:user_id,
        user_session:socket.id,
        room_id:room_id,
        time:time
    } 
    
    // Funçao .on('message') para o recebimento de mensagens
        // Receber a mensagem com username, user_id, msg e time.
        // Plotar na tela a mensagem com diferenciaçao se o user_id for igual ao do usuario.

    */
    
})





