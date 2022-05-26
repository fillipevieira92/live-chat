from flask import Flask, redirect, render_template, request, jsonify, url_for

from backend.services.room import Room
from backend.services.user import User
from backend.controllers.socket import socketController

import json

room = Room()
user = User()

USERNAME = ''
USER_ID = -1
ROOM_ID = -1

def appController(app):
  

    @app.route("/", methods=['GET'])
    def login():
        return render_template("login.html")
    

    @app.route("/login", methods=['POST'])
    def set_username():
        global USERNAME, USER_ID

        USERNAME = request.form.get('username')
        USER_ID = user.create_user(request.form.get('username'))       

        return redirect(url_for('rooms'))

    
    @app.route("/rooms", methods=['GET'])
    def rooms():
        global USERNAME, USER_ID

        return render_template('rooms.html', username=USERNAME, user_id=USER_ID, rooms_list=room.find_all())
    

    @app.route("/rooms", methods=['POST'])
    def set_room():
        global ROOM_ID
        ROOM_ID = room.create_room(request.form.get('sala_nome'))

        return redirect(url_for('rooms'))
        
    