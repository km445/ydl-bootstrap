import os
import logging

import eventlet
from flask import Flask
from flask_socketio import SocketIO

import config
from utils import Log

eventlet.monkey_patch()

app = Flask(__name__)
app.secret_key = config.secret_key
socketio = SocketIO(app, message_queue=config.message_queue)

dirs = [config.downloads_dir, config.logs_dir, config.celery_logs]

[os.mkdir(d) for d in dirs if not os.path.exists(d)]

file_handler = logging.FileHandler(config.log_config.get("filename"))
file_handler.setLevel(config.log_config.get("level"))
file_handler.setFormatter(config.log_config.get("format"))

log = Log(file_handler, "RYDL")
log.info("RYDL service started.")

import blueprints
