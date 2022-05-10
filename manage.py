from distutils.log import debug
from flask import Flask, request, render_template, json
from flask_socketio import SocketIO


app = Flask('__main__')
socket = SocketIO(app)



@app.route('/')
def index():
    return render_template('index.html')




if __name__ == '__main__':
    socket.run(app, '0.0.0.0',8000)
