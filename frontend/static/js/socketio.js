$(document).ready(function(){
    var socket = io('/chat');
    
    const username = document.querySelector('#username').value;
    const user_id = document.querySelector('#user_id').value;
    const room_id = document.querySelector('#room_id').value;
    
    // Ao conectar envia os dados para o servidor.
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


    // Funcao que escuta ao se conectar o callback com todos os usuarios online nesta sala.
    socket.on('online_users', function(data) {
        var peopleOnline = document.querySelector('.people-online');

        for (i=0;i<data.length;i++) {
            var userOnline = document.createElement('div');

            userOnline.innerHTML = `
                <i style="font-size: 1.5rem;" class="bi bi-person-fill"></i>
                <strong class="">${data[i][0]}</strong>
            `

            userOnline.setAttribute('class', 'user-online');
            peopleOnline.appendChild(userOnline);        
        };
    });


    // Funcao que escuta ao se conectar o callback com todas as mensagens antigas.
    socket.on('old_msgs', function(data){
        var chatMsg = document.querySelector('.chat-msgs');
        
        for (i=0;i<data.length;i++) {

            var msgRow = document.createElement('div');
            
            // Se a sala é a mesma da mensagem adiciona a mensagem na tela.
            if (data[i][1] == room_id) {
                
                // Se a mensagem vem de outro usuário adiciona essa mensagem.
                if (data[i][3] != socket.id) {
                    msgRow.innerHTML = `
                    
                        <div class="msg mb-1">
                            <strong class="msg-user">
                                ${data[i][2]}
                            </strong>
                            <p class="msg-body mb-0">
                                ${data[i][4]}
                            </p>
                            <p class="msg-time float-end m-0">
                                ${data[i][5]}
                            </p>
                        </div>
                    
                    `
                } else { // Caso a mensagem seja do usuário adiciona essa mensagem
                    msgRow.innerHTML = `
                    
                        <div class="msg msg-self mb-1">                        
                            <p class="msg-body mb-0">
                                ${data[i][4]}
                            </p>
                            <p class="msg-time float-end m-0">
                                ${data[i][5]}
                            </p>
                        </div>
                    
                    `
                }
                // Adicionando a mensagem na div de mensagens
                msgRow.setAttribute('class', 'msg-row');
                chatMsg.appendChild(msgRow);

                // Rolando o scroll para o fundo.
                chatMsg.scrollTop = chatMsg.scrollHeight;
            }
        }
    })
    

    // Função que escuta as mensagens vinda do servidor.
    socket.on('message', function(data){
        var chatMsg = document.querySelector('.chat-msgs');
        var msgRow = document.createElement('div');

        // Se a sala é a mesma da mensagem adiciona a mensagem na tela.
        if (data.room_id == room_id) {

            // Se a mensagem vem de outro usuário adiciona essa mensagem.
            if (data.user_session != socket.id) {
                
                if (data.msg == 'Acabou de entrar.') {
                    var peopleOnline = document.querySelector('.people-online');        
                    var userOnline = document.createElement('div');
    
                    userOnline.innerHTML = `
                        <i style="font-size: 1.5rem;" class="bi bi-person-fill"></i>
                        <strong class="">${data.username}</strong>
                    `
                    userOnline.setAttribute('class', `user-online ${data.username}`);
                    peopleOnline.appendChild(userOnline);
                }


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
            } else { // Caso a mensagem seja do usuário adiciona essa mensagem
                msgRow.innerHTML = `
                
                    <div class="msg msg-self mb-1">                        
                        <p class="msg-body mb-0">
                            ${data.msg}
                        </p>
                        <p class="msg-time float-end m-0">
                            ${data.time}
                        </p>
                    </div>
                
                `
            }
            // Adicionando a mensagem na div de mensagens
            msgRow.setAttribute('class', 'msg-row');
            chatMsg.appendChild(msgRow);

            // Rolando o scroll para o fundo.
            chatMsg.scrollTop = chatMsg.scrollHeight;
        }
    })

    // Funçao .send para envio de mensagens
    $('#msgSender').on('submit', (e) => {
        e.preventDefault();
        var msgInput = e.target.firstElementChild
        var data = {
            msg:msgInput.value,
            username:username,
            user_id:user_id,
            user_session:socket.id,
            room_id:room_id
        }
        $(msgInput).val('');
        socket.send(data)
    })

    // Usuario se desconectando
    socket.on('user_disconnect', function(data) {
        let userOnline = document.querySelector(`.${data['username']}`);
        userOnline.parentNode.removeChild(userOnline)    

        let chatMsg = document.querySelector('.chat-msgs');
        let msgRow = document.createElement('div');
        msgRow.innerHTML = `
        
            <div class="msg mb-1">
                <strong class="msg-user">
                    ${data['username']}
                </strong>
                <p class="msg-body mb-0">
                    Saiu da conversa.
                </p>
                <p class="msg-time float-end m-0">
                    ${data['time']}
                </p>
            </div>
        
        `
        // Adicionando a mensagem na div de mensagens
        msgRow.setAttribute('class', 'msg-row');
        chatMsg.appendChild(msgRow);

        // Rolando o scroll para o fundo.
        chatMsg.scrollTop = chatMsg.scrollHeight;
    })
})

// Função responsável por adicionar mensagens a tela.
function addMsg(data) {

    
}





