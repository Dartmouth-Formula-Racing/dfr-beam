# main.py - DFR Beam

from flask import Flask
from flask_sockets import Sockets

import logging

app = Flask(__name__)
sockets = Sockets(app)


@sockets.route('/test')
def test(ws):
    while not ws.closed:
        # receive message
        message = ws.receive()

        # check for empty message (disconnected)
        if message is None:
            continue

        logging.debug('Received %s' % message)