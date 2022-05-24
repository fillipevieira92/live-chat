from flask import Flask, redirect, render_template, request, jsonify, url_for
import json

def appController(app):

    @app.route("/", methods=['GET'])
    def login():
        return render_template("login.html")
    

    @app.route("/login", methods=['POST'])
    def set_username():
        return redirect(url_for('room', username=request.form.get('username')))

    
    @app.route("/room", methods=['GET'])
    def room():
        username = request.args['username']
        
        pass
    
    @app.route("/room", methods=['POST'])
    def set_room():
        pass
    