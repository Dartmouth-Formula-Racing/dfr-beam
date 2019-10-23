# main.py - DFR Beam

import logging

from flask import Flask
from flask_sockets import Sockets


app = Flask(__name__)
sockets = Sockets(app)


@sockets.route('/echo')
def echo_socket(ws):
    while not ws.closed:
        # receive message
        message = ws.receive()
        if message is None:
            continue
        
        # log message
        logging.debug(message)
