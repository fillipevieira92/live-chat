from flask import Flask, redirect, render_template, request, jsonify, url_for
from backend.services.room import Room
import json

room_obj = Room()
USERNAME = ''

def appController(app):
  

    @app.route("/", methods=['GET'])
    def login():
        return render_template("login.html")
    

    @app.route("/login", methods=['POST'])
    def set_username():
        global USERNAME
        USERNAME = request.form.get('username')
        return redirect(url_for('rooms'))

    
    @app.route("/rooms", methods=['GET'])
    def rooms():
        
        global USERNAME
        rooms_list = room_obj.find_all()
        return render_template('rooms.html', username=USERNAME, rooms_list=rooms_list)
    
    @app.route("/rooms", methods=['POST'])
    def set_room():
        room_obj.create_room(request.form.get('sala_nome'))
        return redirect(url_for('rooms'))
        
    