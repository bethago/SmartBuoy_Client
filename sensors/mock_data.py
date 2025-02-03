import random

values = {'accelerometer':[0, 0, 0], 'gps':[37.500000, 131.000000, 0.0], 'ultrasonic':[0], 'temperature':[11.0]}

def modify_randomly(values):
    # return [round(value + random.uniform(-0.1, 0.1), 6) for value in values]
    return [round(value + random.uniform(-1, 1), 6) for value in values]

def set_sensors(buoy):
    sensor_datas = buoy.sensors
    for sensor in sensor_datas.keys():
        sensor_datas[sensor] = values[sensor]
    buoy.update_sensors(sensor_datas)

def get_sensor_data(buoy):
    sensor_datas = buoy.sensors
    for sensor, value in sensor_datas.items():
        sensor_datas[sensor] = modify_randomly(value)
    buoy.update_sensors(sensor_datas)

if __name__ == "__main__":
    print("err: Please run main.py.")