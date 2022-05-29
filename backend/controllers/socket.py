from flask import render_template, request, jsonify
from flask_socketio import send, emit
from datetime import datetime

from backend.services.room import Room
from backend.services.user import User
from backend.services.chat import Chat

import json



room = Room()
user = User()
chat = Chat()

USERNAME = ''
USER_ID = None
ROOM_ID = None

def socketController(app, socket):

    # Funçao que renderiza a pagina do chat.
    @app.route('/chat')
    def get_chat_page(username=None, user_id=None, room_id=None):
        global USERNAME, USER_ID, ROOM_ID
        
        try:
            data = json.loads(request.args['data'])
            USERNAME, USER_ID, ROOM_ID = data['username'], data['user_id'], data['room_id']

        except:
            pass
        else:
            return jsonify({'response':'ok'})
        
        if username and user_id and room_id:
            USERNAME, USER_ID, ROOM_ID = username, user_id, room_id
        
        return render_template('room.html', username=USERNAME, user_id=USER_ID, room_id=ROOM_ID)


    # Funcao que desloga o usuário.
    @app.route('/logout')
    def logout():
        time = f'{str(datetime.now().hour - 3).zfill(2)}:{str(datetime.now().minute).zfill(2)}'
        data = json.loads(request.args['data'])

        user.delete_user(data['user_id'], data['room_id'])
        emit('user_disconnect', {"username":data['username'], "time":time}, broadcast=True, namespace='/chat')
        return jsonify({'response':'deleted'})


    # ----------------------- SOCKET EVENTS ----------------------- #
    
    # Funçao que recebe novas conexoes ao socket.
    @socket.on('connect_event', namespace='/chat')
    def connect(data):
        
        time = f'{str(datetime.now().hour - 3).zfill(2)}:{str(datetime.now().minute).zfill(2)}'

        user_data = user.find_user_by_id(data['user_id'])
        print('user_data -> ',user_data[-1])

        user.set_user_room(data['user_id'], data['room_id'])

        # Pegar o id da sala e retornar um emit() contendo o historico das mensagens apenas para quem esta se conectando.
        msg_list = chat.find_all_msgs(data['room_id'])
        online_list = user.get_users_by_room(data['room_id'])
        emit('old_msgs', msg_list)
        emit('online_users', online_list)

        # Enviando a mensagem para todos os usuarios que UserX se conectou.
        user.set_user_session(data['user_session'],data['user_id'])
        
        if not user_data[-1]:
            send({"username":data['username'], "room_id":data['room_id'], "user_session":data['user_session'], "time":time, "msg":"Acabou de entrar."}, broadcast=True)

        

    
    # Função de envio de mensagens para todos os usuarios.
    @socket.on('message', namespace='/chat')
    def message(data):

        time = f'{str(datetime.now().hour - 3).zfill(2)}:{str(datetime.now().minute).zfill(2)}'
        # Pegar as informaçoes do front e guardar na tabela do chat.
        chat.save_message(data, time)
        
        # Pegar essas mesmas informaçoes e retornar em Broadcast para todos os users daquela sala.
        send({"username":data['username'], "room_id":data['room_id'], "user_session":data['user_session'], "time":time, "msg":data['msg']}, broadcast=True)        
        

        
