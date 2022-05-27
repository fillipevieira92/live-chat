from flask import Flask, redirect, render_template, request, jsonify, url_for
from flask_socketio import SocketIO, send, emit
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

    @app.route('/chat')
    def get_chat_page(username=None, user_id=None, room_id=None):
        global USERNAME, USER_ID, ROOM_ID

        try:
            data = json.loads(request.args['data'])
            USERNAME, USER_ID, ROOM_ID = data['username'], data['user_id'], data['room_id']
        except:
            pass
        else:
            return jsonify({'response':200})
        
        if username and user_id and room_id:
            USERNAME, USER_ID, ROOM_ID = username, user_id, room_id

        return render_template('room.html', username=USERNAME, user_id=USER_ID, room_id=ROOM_ID)
        
    # ----------------------- SOCKET EVENTS ----------------------- #
    
    # Funçao que recebe novas conexoes ao socket.
    @socket.on('connect_event', namespace='/chat')
    def connect(data):
        time = f'{str(datetime.now().hour).zfill(2)}:{str(datetime.now().minute).zfill(2)}'
        print('## SOCKET user_id -> ', data['user_id'], USER_ID)
        user.set_user_session(data['user_session'],data['user_id'])
        
        send({"username":data['username'], "user_session":data['user_session'], "time":time, "msg":"Acabou de entrar."}, broadcast=True)
    # TODO: Pegar o id da sala e retornar um send() contendo o historico das mensagens apenas para quem esta se conectando.

    
    # Função de envio de mensagens para todos os usuarios.
    @socket.on('message', namespace='/chat')
    def message(data):
        # TODO: Pegar as informaçoes do front e guardar na tabela do chat.
        # TODO: Pegar essas mesmas informaçoes e retornar em Broadcast para todos os users daquela sala.
        
        pass

        
