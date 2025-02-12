import configparser

class Server:
    def __init__(self):
        self.ipaddr = None
        self.port = None
        self.cse_base = None
        self.url = None

    def set_ip(self, ipaddr):
        self.ipaddr = ipaddr

    def set_port(self, port):
        self.port = port

    def set_cse_base(self, cse_base):
        self.cse_base = cse_base

    def set_url(self):
        self.url = f"http://{self.ipaddr}:{self.port}/{self.cse_base}"

class Buoy:
    def __init__(self):
        self.buoy_name = None
        self.mock = False
        self.sensors = dict()

    def set_buoy_name(self, buoy_name):
        self.buoy_name = buoy_name

    def set_mock(self, mock):
        if mock == "TRUE":
            self.mock = True

    def set_sensors(self, sensors):
        for sensor, status in sensors:
            if status == "TRUE":
                self.sensors[sensor] = None

    def update_sensors(self, sensors):
        self.sensors.update(sensors)

def read_config():
    server = Server()
    buoy = Buoy()

    config = configparser.ConfigParser()
    config.read('config.ini')

    try:
        # set CSE server info
        server.set_ip(config['CSE SERVER']['server ip'])
        server.set_port(config['CSE SERVER']['server port'])
        server.set_cse_base(config['CSE SERVER']['cse base'])
        server.set_url()

        # set Buoy info
        buoy.set_buoy_name(config['BUOY']['buoy name'])
        buoy.set_mock(config['BUOY']['mock'])
        buoy.set_sensors(config.items('SENSORS'))

    except Exception as e:
        print(f"ERROR occurred: {e}. Please check config.ini.")

    return server, buoy

config = configparser.ConfigParser()
config.read('config.ini')
X_M2M_ORIGIN = config['BUOY']['origin']

if __name__ == "__main__":
    print("err: Please run main.py.")