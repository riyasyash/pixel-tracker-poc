from flask import Flask, request, send_from_directory
from urllib.request import urlopen
from datetime import datetime
from googlesheets import *
import json
# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')

@app.route('/')
def send_js():
    ip =""
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return send_from_directory('', 'image.gif')

if __name__ == "__main__":
    app.run()