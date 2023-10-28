from flask import Flask, render_template, request
# from flask_cors import CORS
import atexit
from config import Config 
from printer import Printer
from cleaning import Cleaning

app = Flask(__name__)
# CORS(app, resources={r'/*': {'origins': '*'}})
app_config = Config('app.config')
print(app_config.dry_cycle.dry.motor_setting.speed)
app_printer = Printer();
app_cleaning = Cleaning()
def startCleaningProcess():
    if app_printer.prepare_printer():
        app_cleaning.clean()

def restartFirware():
    return app_printer.app_moonraker_util.firmware_restart()

def homePrinter(): 
    return app_printer.home_printer()
          
    
@app.route("/", methods=['GET', 'POST'])
def index():
    templateData = {}
    cleaning_status = 'Off'
    firmware_restart_status = ''
    firmware_state = ''
    firmware_message = ''
    homing_state = ''
    if request.method == 'POST':
        if request.form.get('start') == 'Start Cleaning':
            cleaning_status = 'Start'
            startCleaningProcess()
        if request.form.get('restart_firmware') == 'Restart Firmware':
            res = restartFirware();
            print(res)
            firmware_restart_status = 'Starting'
            while True:
                react_dict = app_printer.app_moonraker_util.server_get("/printer/info")
                if('result' in react_dict):
                    break
        if request.form.get('home') == 'Home':
            homing_state = 'Homing'
            while True:
                react_dict = homePrinter()
                if(app_printer.app_moonraker_util.is_printer_homed):
                    break
    react_dict = app_printer.app_moonraker_util.server_get("/printer/info")
    if('result' in react_dict):
        firmware_state = react_dict['result']['state']
        firmware_message = react_dict['result']['state_message']

    if(app_printer.app_moonraker_util.is_printer_homed):
        homing_state = 'Homed'
    else: 
        homing_state = 'Not Homed'        
    templateData = {'firmware_state': firmware_state, 'firmware_message': firmware_message, 'cleaning_status': cleaning_status, 'restart_status': firmware_restart_status, 'homing_state': homing_state}
    print(templateData)
    return render_template('index.html', **templateData)

def exit_handler():
    app_cleaning.app_motor.clean_up()
atexit.register(exit_handler) 

if __name__ == '__main__':
    app.run(host='0.0.0.0')