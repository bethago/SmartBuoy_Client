# execute this file
from utils import init
from utils import oneM2M

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
        cnt_rn = "sensor1"
        if not oneM2M.check_cnt(server.url, buoy.buoy_name, cnt_rn):
            print(f"failed to find the CNT {cnt_rn}")

        sensor_value = "123"
        if not oneM2M.create_cin(server.url, buoy.buoy_name, cnt_rn, sensor_value):
            print(f"failed to create cin")

        print("success!")

        headers = oneM2M.Headers(ri='retrieve_cin_all')
        response = oneM2M.requests.get(f"{server.url}/{buoy.buoy_name}/{cnt_rn}?fu=1&ty=4&lbl={cnt_rn}", headers=headers.headers)
        print(response.json())

    else:   # run with sensors (realtime). TBD.
        pass