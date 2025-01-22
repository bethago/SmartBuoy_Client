import requests

### Headers
class Headers:
    def __init__(self, ri='please_set_ri', content_type=None):
        self.headers = {
            'Accept': 'application/json',
            'X-M2M-Origin': 'CAdmin',
            'Content-Type': 'application/json',
            'X-M2M-RVI': '3',
            'X-M2M-RI': ri
        }
        if content_type:
            self.set_content_type(content_type)

    def set_content_type(self, content_type):
        ty = self.get_content_type(content_type)
        if ty is None:
            raise ValueError(f"Invalid content type: {content_type}")
        self.headers['Content-Type'] = f"application/json;ty={ty}"

    @staticmethod
    def get_content_type(content_type):
        types = {
            'ae': 2,
            'cnt': 3,
            'cin': 4,
            'cb': 5
        }
        return types.get(content_type, None)

### Retrieve CSE Base
def check_cse(url):
    headers = Headers(ri='retrieve_cse_base', content_type='cb')
    try:
        response = requests.get(url, headers=headers.headers)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(f"ERROR occurred: {e}")
        return False

def check_ae(url, ae_rn):
    headers = Headers(ri='retrieve_ae', content_type='ae')
    try:
        response = requests.get(f"{url}/{ae_rn}", headers=headers.headers)
        if response.status_code == 200:
            return True
        else:
            headers.headers['X-M2M-RI'] = 'create_ae'
            body = {
                "m2m:ae": {
                    "rn": ae_rn,
                    "api": "NBuoy",
                    "rr": True,
                    "lbl": ["buoy1", "test"],
                    "srv": ["3"]
                }
            }
            try:
                response = requests.post(url, headers=headers.headers, json=body)
                if response.status_code == 201:
                    return True
                else:
                    print(f"ERROR occurred: Response status: {response.status_code}")
                    return False
            except requests.exceptions.RequestException as e:
                print(f"ERROR occurred: {e}")
                return False
    except requests.exceptions.RequestException as e:
        print(f"ERROR occurred: {e}")
        return False

def check_cnt(url, ae_rn, cnt_rn):
    headers = Headers(ri='retrieve_cnt', content_type='cnt')
    try:
        response = requests.get(f"{url}/{ae_rn}/{cnt_rn}", headers=headers.headers)
        if response.status_code == 200:
            return True
        else:
            headers.headers['X-M2M-RI'] = 'create_cnt'
            body = {
                "m2m:cnt": {
                    "rn": cnt_rn,
                    "lbl": ["sensor", cnt_rn],
                }
            }
            try:
                response = requests.post(f"{url}/{ae_rn}", headers=headers.headers, json=body)
                if response.status_code == 201:
                    return True
                else:
                    print(f"ERROR occurred: Response status: {response.status_code}")
                    return False
            except requests.exceptions.RequestException as e:
                print(f"ERROR occurred: {e}")
                return False
    except requests.exceptions.RequestException as e:
        print(f"ERROR occurred: {e}")
        return False

def create_cin(url, ae_rn, cnt_rn, sensor_value):
    headers = Headers(ri='create_cin', content_type='cin')
    body = {
        "m2m:cin": {
            "con": sensor_value,
            "lbl": ["value", cnt_rn],
        }
    }
    try:
        response = requests.post(f"{url}/{ae_rn}/{cnt_rn}", headers=headers.headers, json=body)
        if response.status_code == 201:
            return True
        else:
            print(f"ERROR occurred: Response status: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"ERROR occurred: {e}")
        return False

if __name__ == "__main__":
    print("err: Please run main.py.")