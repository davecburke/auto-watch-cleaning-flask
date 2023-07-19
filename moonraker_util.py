import requests

class Moonraker_Util():
    def __init__(self, server_url):
        self.server_url = server_url
    
    def is_klippy_connected(self):
        print('KLIPPY CONNECTED')
        return self.get_klippy_connected_status()
    
    def is_klippy_ready(self):
        print('KLIPPY READY')
        return self.get_klippy_state() == 'ready'
    
    def is_printer_homed(self):
        return self.get_homed_status() == 'xyz'
    
    def get_klippy_connected_status(self):
        response_dict = self.server_get("/server/info")
        return response_dict['result']['klippy_connected']

    def get_klippy_state(self):
        response_dict = self.server_get("/printer/info")
        return response_dict['result']['state']
    
    def get_klippy_state_message(self):
        response_dict = self.server_get("/printer/info")
        return response_dict['result']['state_message']
    
    def firmware_restart(self):
        response_dict = self.server_post("/printer/firmware_restart")
        return response_dict['result']

    def get_homed_status(self):
        response_dict = self.server_get("/printer/objects/query?toolhead")
        return response_dict['result']['status']['toolhead']['homed_axes']
    
    def server_get(self, query):
        return requests.get(self.server_url + query).json()  

    def server_post(self, query):
        return requests.post(self.server_url + query).json() 
    
    def send_gcode(self, gcode):
        return self.server_post('/printer/gcode/script?script=' + gcode)
    
    def tool_head_position(self):
        resp_dict = self.server_get('/printer/objects/query?toolhead');
        print(resp_dict)
        print(resp_dict['status']['toolhead']['position'])
        return resp_dict['status']['toolhead']['position']

