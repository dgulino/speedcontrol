from flask import Flask, send_from_directory, request, render_template
from easyprocess import EasyProcess
import json

app = Flask(__name__)

CLI = "/usr/share/speedify/speedify_cli"

@app.route('/get_toggled_status') 
def toggled_status():
  current_status = request.args.get('status')
  print(current_status)
  if current_status == 'DISCONNECTED':
      result = EasyProcess([CLI,"connect"]).call().stdout
      return 'CONNECTED'  
  else:
      result = EasyProcess([CLI,"disconnect"]).call().stdout
      return 'DISCONNECTED'

@app.route('/status')
def status():
    result = EasyProcess([CLI,"state"]).call().stdout
    result = json.loads(result)
    state = result.get('state')
    print(state)
    if state == "CONNECTED":
        return "CONNECTED"
    else:
        return "DISCONNECTED"

@app.route('/connect')
def connect():
    if 'status' in request.args:
        if request.args['status'] == 'CONNECT':
            result = EasyProcess([CLI,"connect"]).call().stdout
            return "CONNECTED"
        if request.args['status'] == 'DISCONNECT':
            result = EasyProcess([CLI,"disconnect"]).call().stdout
            return "DISCONNECTED"

@app.route("/")
def index():
    state = status()
    if state == "CONNECTED":
        checked = "checked"
    else:
        checked = ""

    return render_template('index.html', checked = checked, status = state)

