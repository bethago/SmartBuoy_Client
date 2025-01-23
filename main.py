# execute this file
from utils import init
from utils import oneM2M
from sensors import mock_data
from time import sleep

def run():
    pass

# main
if __name__ == '__main__':
    server, buoy = init.read_config()

    if not oneM2M.check_cse(server.url):
        print(f"{buoy.buoy_name}: Unable to find the CSE Base. please check if the CSE Base is online.")
        exit()

    if not oneM2M.check_ae(server.url, buoy.buoy_name):
        print(f"Unable to find the AE {buoy.buoy_name}.")
        exit()

    if buoy.mock:   # buoy.mock == True
        cnt_rn = ["accelerometer", "gps", "ultrasonic"]
        for rn in cnt_rn:
            if not oneM2M.check_cnt(server.url, buoy.buoy_name, rn):
                print(f"failed to find the CNT {rn}")

        datas = mock_data.get_sensor_data()
        for i in range(10):
            # print(list(map(str, datas)))
            cin_value = list(map(str, datas))
            for rn, value in zip(cnt_rn, cin_value):
                if not oneM2M.create_cin(server.url, buoy.buoy_name, rn, value):
                    print(f"failed to create cin for {rn}")
            for rn in cnt_rn:
                response = oneM2M.requests.get(f"{server.url}/{buoy.buoy_name}/{rn}?fu=1&ty=4&lbl={rn}", headers=oneM2M.Headers(ri='retrieve_cin_all').headers)
                print(response.json())
            sleep(10)
            datas = mock_data.get_sensor_data(datas)

    else:   # run with sensors (realtime). TBD.
        pass