# sensors list
## accelerometer
## gps
## ultrasonic
## temperature

import RPi.GPIO as GPIO
import smbus
from gps3 import gps3
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
TRIG = 23
ECHO = 24
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

bus = smbus.SMBus(1)
address = 0x53
bus.write_byte_data(address, 0x2D, 0x08)

gps_socket = gps3.GPSDSocket()
data_stream = gps3.DataStream()
gps_socket.connect()
gps_socket.watch()

def get_distance(): # ultrasonic
    GPIO.output(TRIG, False)
    time.sleep(0.1)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)

    return distance

def read_accel():   # accelerometer
    data = bus.read_i2c_block_data(address, 0x32, 6)
    x = (data[1] << 8) | data[0]
    y = (data[3] << 8) | data[2]
    z = (data[5] << 8) | data[4]

    if x & (1 << 15):
        x -= 1 << 16
    if y & (1 << 15):
        y -= 1 << 16
    if z & (1 << 15):
        z -= 1 << 16

    return [x, y, z]

def get_gps_data(): # gps
    latitude, longitude, altitude = None, None, None
    for new_data in gps_socket:
        if new_data:
            data_stream.unpack(new_data)
            latitude = data_stream.TPV['lat']
            longitude = data_stream.TPV['lon']
            altitude = data_stream.TPV['alt']
            if latitude is not None and longitude is not None and altitude is not None:
                return latitude, longitude, altitude
        break
    return [latitude, longitude, altitude]

def get_sensor_data(buoy):
    sensor_datas = buoy.sensors
    for sensor in sensor_datas.keys():
        match sensor:
            case 'accelerometer':
                sensor_datas[sensor] = read_accel()
            case 'gps':
                sensor_datas[sensor] = get_gps_data()
            case 'ultrasonic':
                sensor_datas[sensor] = get_distance()
            case _:
                sensor_datas[sensor] = 0
    buoy.update_sensors(sensor_datas)

if __name__ == "__main__":
    print("err: Please run main.py.")