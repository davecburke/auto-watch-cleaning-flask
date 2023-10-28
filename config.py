import configparser

class Config():
    def __init__(self, config_file_path):
        self.config_file = configparser.ConfigParser()
        self.config_file.read(config_file_path, 'utf-8')
        self.moonraker_ip = self.config_file['moonraker']['ip_address']
        self.pause_after_move = int(self.config_file['general']['pause_after_move'])
        self.clean_cycle = self.Clean_Cycle(self.config_file['clean_cycle'], self.config_file['clean_cycle_wash'],self.config_file['clean_cycle_expel'])
        self.rinse_cycle_1 = self.Clean_Cycle(self.config_file['rinse_cycle_1'], self.config_file['rinse_cycle_1_wash'],self.config_file['rinse_cycle_1_expel'])
        self.rinse_cycle_2 = self.Clean_Cycle(self.config_file['rinse_cycle_2'], self.config_file['rinse_cycle_2_wash'],self.config_file['rinse_cycle_2_expel'])
        self.dry_cycle = self.Dry_Cycle(self.config_file['dry_cycle'], self.config_file['dry_cycle_spin'])
        
    def motor_control_input_1(self):
        return int(self.config_file['motor_gpio_pins']['motor_control_input_1'])
    
    def motor_control_input_2(self):
        return int(self.config_file['motor_gpio_pins']['motor_control_input_2'])
    
    def motor_enable(self):
        return int(self.config_file['motor_gpio_pins']['motor_enable'])
    
    def heater_fan_control_input_1(self):
        return int(self.config_file['heater_gpio_pins']['heater_fan_control_input_1'])
    
    def heater_fan_control_input_2(self):
        return int(self.config_file['heater_gpio_pins']['heater_fan_control_input_2'])
    
    def heater_fan_enable(self):
        return int(self.config_file['heater_gpio_pins']['heater_fan_enable'])
    
    def heater_element(self):
        return int(self.config_file['heater_gpio_pins']['heater_element'])
    
    class Cycle:
        def __init__(self, cycle):
            self.receptacle = self.Receptacle(cycle)
        class Receptacle:
            def __init__(self, cycle):
                self.location_x = int(cycle['receptacle_location_x'])
                self.location_y = int(cycle['receptacle_location_y'])
                self.location_wash_z = int(cycle['receptacle_location_wash_z'])
                self.location_expel_z = int(cycle['receptacle_location_expel_z'])
                self.receptacle_clearance = (int(cycle['receptacle_clearance']))
        
        class Cycle_Stage:
            def __init__(self, cycle): 
                self.duration = float(cycle['duration'])
                self.mode = cycle['mode']
                self.motor_setting = self.Motor_Setting()
                if cycle['mode'] == 'agitate':
                    self.motor_setting.speed_forward = cycle['speed_forward']
                    self.motor_setting.time_forward = cycle['time_forward']
                    self.motor_setting.time_brake_forward = cycle['time_brake_forward']
                    self.motor_setting.speed_backward = cycle['speed_backward']
                    self.motor_setting.time_backward = cycle['time_backward']
                    self.motor_setting.time_brake_backward = cycle['time_brake_backward']
                else:
                    self.motor_setting.speed = cycle['speed']
                    self.motor_setting.direction = cycle['direction']

            class Motor_Setting:
                @property
                def speed_forward(self):
                    return self._speed_forward
                
                @speed_forward.setter
                def speed_forward(self, value):
                    self._speed_forward = float(value)

                @property
                def time_forward(self):
                    return self._time_forward
                
                @time_forward.setter
                def time_forward(self, value):
                    self._time_forward = float(value)    
                
                @property
                def time_brake_forward(self):
                    return self._time_brake_forward
                
                @time_brake_forward.setter
                def time_brake_forward(self, value):
                    self._time_brake_forward = float(value)

                @property
                def speed_backward(self):
                    return self._speed_backward
                
                @speed_backward.setter
                def speed_backward(self, value):
                    self._speed_backward = float(value)

                @property
                def time_backward(self):
                    return self._time_backward
                
                @time_backward.setter
                def time_backward(self, value):
                    self._time_backward = float(value)    
                
                @property
                def time_brake_backward(self):
                    return self._time_brake_backward
                
                @time_brake_backward.setter
                def time_brake_backward(self, value):
                    self._time_brake_backward = float(value)    
                
                @property
                def direction(self):
                    return self._direction
                
                @direction.setter
                def direction(self, value):
                    self._direction = value    
                
                @property
                def speed(self):
                    return self._speed
                
                @speed.setter
                def speed(self, value):
                    self._speed = float(value)

    class Clean_Cycle(Cycle):
        def __init__(self, cycle, cycle_wash, cycle_expel):
            super().__init__(cycle)
            self.wash = self.Cycle_Stage(cycle_wash)
            self.expel = self.Cycle_Stage(cycle_expel)

    class Dry_Cycle(Cycle):
        def __init__(self, cycle, cycle_dry):
            super().__init__(cycle)
            self.dry = self.Cycle_Stage(cycle_dry)

