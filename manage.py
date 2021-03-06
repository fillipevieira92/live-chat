from flask import Flask
from flask_socketio import SocketIO

from backend.controllers.app import appController
from backend.controllers.socket import socketController


app = Flask('__main__', template_folder='frontend/templates', static_folder='frontend/static')

socket = SocketIO(app)

appController(app)
socketController(app, socket)


if __name__ == '__main__':
    socket.run(app, '0.0.0.0',8000, debug=True)
