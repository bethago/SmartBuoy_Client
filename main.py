# execute this file
from utils import init
from utils import oneM2M
from sensors import mock_data
# from sensors import sensors
from time import sleep

# main
if __name__ == '__main__':
    server, buoy = init.read_config()

    if not oneM2M.check_cse(server.url):
        print(f"{buoy.buoy_name}: Unable to find the CSE Base. please check if the CSE Base is online.")
        exit()

    if not oneM2M.check_ae(server.url, buoy.buoy_name):
        print(f"Unable to create the AE {buoy.buoy_name}.")
        exit()

    for sensor in buoy.sensors:
        if not oneM2M.check_cnt(server.url, buoy.buoy_name, sensor):
            print(f"failed to create the CNT {sensor}")
            exit()

    if not oneM2M.check_grp(server.url, server.cse_base, buoy.buoy_name, buoy.sensors.keys()):
        print(f"failed to create the GRP grp_{buoy.buoy_name}")
        exit()

    fetch_data = None
    if buoy.mock:   # buoy.mock == True
        mock_data.set_sensors(buoy)
        fetch_data = mock_data.get_sensor_data

    else:   # run with sensors (realtime).
        # fetch_data = sensors.get_sensor_data(buoy)
        pass

    while True:
        fetch_data(buoy)
        for sensor, value in buoy.sensors.items():
            if not oneM2M.create_cin(server.url, buoy.buoy_name, sensor, str(value)):
                print(f"failed to create cin for {sensor}")
            else:
                print(f"created cin for {sensor}")
        sleep(1)
