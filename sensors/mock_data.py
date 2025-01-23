import random

accelerometer_value = [0, 0, 0]
gps_value = [37.500000, 131.000000, 0.0]
ultrasonic_value = [0]

sensor_datas = [accelerometer_value, gps_value, ultrasonic_value]

def modify_randomly(values):
    return [round(value + random.uniform(-0.1, 0.1), 6) for value in values]

def get_sensor_data(datas = sensor_datas):
    for i in range(len(datas)):
        datas[i] = modify_randomly(datas[i])
    return datas

if __name__ == "__main__":
    print("err: Please run main.py.")