from flask import Flask, redirect, render_template, request, jsonify, url_for
import json

def appController(app):

    @app.route("/", methods=['GET'])
    def login():
        return render_template("login.html")
    

    @app.route("/login", methods=['POST'])
    def set_username():
        return redirect(url_for('room', username=request.form.get('username')))

    
    @app.route("/rooms", methods=['GET'])
    def room():
        username = request.args['username']
        
        return render_template('rooms.html', username=username)
    
    @app.route("/rooms", methods=['POST'])
    def set_room():
        pass
    