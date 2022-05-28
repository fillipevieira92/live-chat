from flask import Flask, redirect, render_template, request, jsonify, url_for

from backend.services.room import Room
from backend.services.user import User

import json



room = Room()
user = User()

USERNAME = ''
USER_ID = -1
ROOM_ID = -1

def appController(app):
  
    # Funçao que trás a tela de login.
    @app.route("/", methods=['GET'])
    def login():
        return render_template("login.html")
    

    # Funçao para validar o username.
    @app.route("/ajax", methods=['GET'])
    def valid_username():

        username_exists = None

        try:
            username_exists = user.find_user_by_username(json.loads(request.args['username']))
        except:
            username_exists = None

        if username_exists:
            return jsonify({"response":"Já existe um usuário com esse nome."})
        else:
            return jsonify({"response":"ok"})
        

    # Funçao para criar o usuário.
    @app.route("/login", methods=['POST'])
    def set_username():
        global USERNAME, USER_ID

        USERNAME = request.form.get('username')
        USER_ID = user.create_user(request.form.get('username'))       

        return redirect(url_for('rooms'))


    # Funcao que trás a pagina de salas.
    @app.route("/rooms", methods=['GET'])
    def rooms():
        global USERNAME, USER_ID

        return render_template('rooms.html', username=USERNAME, user_id=USER_ID, rooms_list=room.find_all())
    

    # Funcao para criar uma sala.
    @app.route("/rooms", methods=['POST'])
    def set_room():
        global ROOM_ID
        ROOM_ID = room.create_room(request.form.get('sala_nome'))

        return redirect(url_for('rooms'))
        
    