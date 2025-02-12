import random

values = {'accelerometer':[0, 0, 0], 'gps':[37.500000, 131.000000, 0.0], 'ultrasonic':[0], 'temperature':[11.0]}

def modify_randomly(values):
    new_values = []
    for value in values:
        # modified_value = round(value + random.uniform(-0.1, 0.1), 6)
        modified_value = round(value + random.uniform(-5, 5), 6)
        if modified_value < 0:
            modified_value = 0
        new_values.append(modified_value)
    return new_values

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