from flask import Flask, redirect, render_template, request, jsonify, url_for
from flask_socketio import SocketIO, send, emit

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
    @socket.on('connect_event', namespace='/chat')
    def connect(data):
        user.set_user_session(data['user_session'],data['user_id'])
        socket.emit('teste')



        
