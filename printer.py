from moonraker_util import Moonraker_Util
from config import Config
import datetime 
class Printer():
    def __init__(self):
        self.app_config = Config('app.config')
        self.app_moonraker_util = Moonraker_Util(self.app_config.moonraker_ip)

    def prepare_printer(self):
        print('PREPARE')
        if(self.app_moonraker_util.is_klippy_connected() and self.app_moonraker_util.is_klippy_ready()):
            print('READY')
            if(self.app_moonraker_util.is_printer_homed()):
                print('HOMED')
                return True
            else:
                self.home_printer()
                if(self.app_moonraker_util.is_printer_homed()):
                    return True
                else:
                    return False
        else:
            print('NOT READY')
            return False    
        
    def printer_ready(self):
        return self.app_moonraker_util.is_printer_homed() == True and self.app_moonraker_util.is_klippy_connected() == True and self.app_moonraker_util.is_klippy_ready() == True
    
    def home_printer(self):
        return self.app_moonraker_util.send_gcode('G28')

    # def motor_controller_power_on(self):
    #     return self.app_moonraker_util.send_gcode('M106 S255')
    
    # def motor_controller_power_off(self):
    #     return self.app_moonraker_util.send_gcode('M107')
    
    def move_to(self, x=None, y=None, z=None):
        co_ords = ''
        if(not(x is None)):
            if(co_ords == ''):
                co_ords += 'X' + str(x)
            else:
                co_ords += ' X' + str(x)
        if(not(y is None)):
            if(co_ords == ''):
                co_ords += 'Y' + str(y)
            else:
                co_ords += ' Y' + str(y)        
        if(not(z is None)):
            if(co_ords == ''):
                co_ords += 'Z' + str(z)
            else:
                co_ords += ' Z' + str(z)
        return self.app_moonraker_util.send_gcode('G0 ' + co_ords)
    
    def tool_head_position(self):
        return self.app_moonraker_util.tool_head_position

    def complete_moves(self):
        return self.app_moonraker_util.send_gcode('M400')
    
    def complete_move_and_pause(self):
        print('CALL COMPLETE MOVES')
        resp_dict = self.complete_moves();
        print(resp_dict)
        if('result' not in resp_dict or resp_dict['result'] != 'ok'):
            return False
        
        endTime = datetime.datetime.now() + datetime.timedelta(seconds=self.app_config.pause_after_move)
        while True:
            if datetime.datetime.now() >= endTime:
                break
            pass
        return True    
