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
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
       ip = request.environ['REMOTE_ADDR']
    else:
        ip = request.environ['HTTP_X_FORWARDED_FOR']
    with urlopen("https://geolocation-db.com/jsonp/"+ip) as url:
                datay = url.read().decode()
                datay = datay.split("(")[1].strip(")")
                data = json.loads(datay)
                writeToSheet([[current_time,ip,data["country_code"],data["city"],data["state"],data["postal"],request.headers.get('User-Agent')]])
    return send_from_directory('', 'image.gif')

if __name__ == "__main__":
    app.run()