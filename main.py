# main.py - DFR Beam

import logging

from flask import Flask
from flask_sockets import Sockets


app = Flask(__name__)
sockets = Sockets(app)


@sockets.route('/')
def root_socket(ws):
    while not ws.closed:
        # receive message
        message = ws.receive()
        if message is None:
            continue

        # bounce message to all connected clients
        clients = ws.handler.server.clients.values()
        for client in clients:
            client.ws.send(message)
