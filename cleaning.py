from time import sleep
import datetime

from motor import Motor
from printer import Printer
from config import Config 
class Cleaning():
    def __init__(self):
        self.app_config = Config('app.config')
        self.app_motor = Motor(self.app_config.motor_control_input_1(), self.app_config.motor_control_input_2(), self.app_config.motor_enable())
        self.app_printer = Printer()   
    def clean(self):
        #turn on power to motor control
        self.app_printer.motor_controller_power_on()
        
        #clean cycle
        print('CLEAN')
        print('WASH')
        receptacle_co_ords = self.app_config.clean_cycle.receptacle
        #move to receptacle
        resp_dict = self.app_printer.move_to(receptacle_co_ords.location_x, receptacle_co_ords.location_y, None)
        if('result' not in resp_dict or resp_dict['result'] != 'ok'):
            return False

        resp_dict = self.app_printer.move_to(None, None, receptacle_co_ords.location_wash_z)
        if('result' not in resp_dict or resp_dict['result'] != 'ok'):
            return False
        
        move_and_pause = self.app_printer.complete_move_and_pause()
        if(not(move_and_pause)):
            return False

        wash = self.app_config.clean_cycle.wash
        if wash.mode == 'agitate':
            print('call agitate')
            self.agitate(wash.duration, wash.motor_setting.speed_forward, wash.motor_setting.time_forward, wash.motor_setting.time_brake_forward, wash.motor_setting.speed_backward, wash.motor_setting.time_backward, wash.motor_setting.time_brake_backward)
        else:
            self.spin(wash.duration, wash.motor_setting.speed)
        
        move_and_pause = self.app_printer.complete_move_and_pause()
        if(not(move_and_pause)):
            return False

        print('EXPEL')
        self.app_printer.move_to(None, None, receptacle_co_ords.location_expel_z)
        move_and_pause = self.app_printer.complete_move_and_pause()
        if(not(move_and_pause)):
            return False
        expel = self.app_config.clean_cycle.expel
        if expel.mode == 'agitate':
            self.agitate(expel.duration, expel.motor_setting.speed_forward, expel.motor_setting.time_forward, expel.motor_setting.time_brake_forward, expel.motor_setting.speed_backward, expel.motor_setting.time_backward, expel.motor_setting.time_brake_backward)
        else:
            self.spin(expel.duration, expel.motor_setting.direction, expel.motor_setting.speed)
        move_and_pause = self.app_printer.complete_move_and_pause()
        if(not(move_and_pause)):
            return False

        self.app_printer.move_to(None, None, receptacle_co_ords.location_expel_z + receptacle_co_ords.receptacle_clearance)
        move_and_pause = self.app_printer.complete_move_and_pause()
        if(not(move_and_pause)):
            return False

        #rinse cycle 1
        print('RINSE 1')
        print('WASH')
        receptacle_co_ords = self.app_config.rinse_cycle_1.receptacle
        #move to receptacle
        self.app_printer.move_to(receptacle_co_ords.location_x, receptacle_co_ords.location_y, None)
        self.app_printer.move_to(None, None, receptacle_co_ords.location_wash_z)
        move_and_pause = self.app_printer.complete_move_and_pause()
        if(not(move_and_pause)):
            return False
        
        wash = self.app_config.rinse_cycle_1.wash
        if wash.mode == 'agitate':
            self.agitate(wash.duration, wash.motor_setting.speed_forward, wash.motor_setting.time_forward, wash.motor_setting.time_brake_forward, wash.motor_setting.speed_backward, wash.motor_setting.time_backward, wash.motor_setting.time_brake_backward)
        else:
            self.spin(wash.duration, wash.motor_setting.speed)
        move_and_pause = self.app_printer.complete_move_and_pause()
        if(not(move_and_pause)):
            return False
        print('EXPEL')
        self.app_printer.move_to(None, None, receptacle_co_ords.location_expel_z)
        move_and_pause = self.app_printer.complete_move_and_pause()
        if(not(move_and_pause)):
            return False

        expel = self.app_config.rinse_cycle_1.expel
        if expel.mode == 'agitate':
            self.agitate(expel.duration, expel.motor_setting.speed_forward, expel.motor_setting.time_forward, expel.motor_setting.time_brake_forward, expel.motor_setting.speed_backward, expel.motor_setting.time_backward, expel.motor_setting.time_brake_backward)
        else:
            self.spin(expel.duration, expel.motor_setting.direction, expel.motor_setting.speed)
        move_and_pause = self.app_printer.complete_move_and_pause()
        if(not(move_and_pause)):
            return False
        self.app_printer.move_to(None, None, receptacle_co_ords.location_expel_z + receptacle_co_ords.receptacle_clearance)
        move_and_pause = self.app_printer.complete_move_and_pause()
        if(not(move_and_pause)):
            return False
        
        #rinse cycle 2
        print('RINSE 2')
        print('WASH')
        receptacle_co_ords = self.app_config.rinse_cycle_2.receptacle
        #move to receptacle
        self.app_printer.move_to(receptacle_co_ords.location_x, receptacle_co_ords.location_y, None)
        self.app_printer.move_to(None, None, receptacle_co_ords.location_wash_z)
        move_and_pause = self.app_printer.complete_move_and_pause()
        if(not(move_and_pause)):
            return False
        wash = self.app_config.rinse_cycle_2.wash
        if wash.mode == 'agitate':
            self.agitate(wash.duration, wash.motor_setting.speed_forward, wash.motor_setting.time_forward, wash.motor_setting.time_brake_forward, wash.motor_setting.speed_backward, wash.motor_setting.time_backward, wash.motor_setting.time_brake_backward)
        else:
            self.spin(wash.duration, wash.motor_setting.speed)
        
        move_and_pause = self.app_printer.complete_move_and_pause()
        if(not(move_and_pause)):
            return False
        print('EXPEL')
        self.app_printer.move_to(None, None, receptacle_co_ords.location_expel_z)
        move_and_pause = self.app_printer.complete_move_and_pause()
        if(not(move_and_pause)):
            return False
        expel = self.app_config.rinse_cycle_2.expel
        if expel.mode == 'agitate':
            self.agitate(expel.duration, expel.motor_setting.speed_forward, expel.motor_setting.time_forward, expel.motor_setting.time_brake_forward, expel.motor_setting.speed_backward, expel.motor_setting.time_backward, expel.motor_setting.time_brake_backward)
        else:
            self.spin(expel.duration, expel.motor_setting.direction, expel.motor_setting.speed)                    
        move_and_pause = self.app_printer.complete_move_and_pause()
        if(not(move_and_pause)):
            return False
        self.app_printer.move_to(None, None, receptacle_co_ords.location_expel_z + receptacle_co_ords.receptacle_clearance)
        move_and_pause = self.app_printer.complete_move_and_pause()
        if(not(move_and_pause)):
            return False
        self.app_printer.motor_controller_power_off()
        self.app_printer.home_printer()
        self.app_printer.move_to(None, None, 340)
        # self.app_motor.clean_up()
        

    def agitate(self, duration, speed_forward, time_forward, time_brake_forward, speed_backward, time_backward, time_brake_backward):
        endTime = datetime.datetime.now() + datetime.timedelta(seconds=duration)
        while True:
            if datetime.datetime.now() >= endTime:
                break
            print('agitate')
            self.app_motor.brake()
            sleep(time_brake_backward)
            self.app_motor.forward(speed_forward)
            sleep(time_forward)
            self.app_motor.brake()
            sleep(time_brake_forward)
            self.app_motor.backward(speed_backward)
            sleep(time_backward)
        self.app_motor.brake()    

    def spin(self, duration, direction, speed):
        endTime = datetime.datetime.now() + datetime.timedelta(seconds=duration)
        self.app_motor.brake()
        while True:
            if datetime.datetime.now() >= endTime:
                break
            if direction == 'forward':
                self.app_motor.forward(speed)
            else:
                self.app_motor.backward(speed)
        
        self.app_motor.brake()