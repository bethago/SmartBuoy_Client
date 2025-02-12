import requests

URL = "http://127.0.0.1:3000/TinyIoT/defaultACP"
CLIENTS = ["CBUOY1", "CBUOY2", "CBUOY3", "CBUOY4"]

header = {
    'Accept': 'application/json',
    'X-M2M-Origin': 'CAdmin',
    'Content-Type': 'application/json;ty=1',
    'X-M2M-RVI': '3',
    'X-M2M-RI': 'update_acp'
}
body = {
    "m2m:acp": {
        "pv": {
            "acr": [
                {
                    "acor": CLIENTS,
                    "acop": 35
                },
                {
                    "acor": [
                        "CServer"
                    ],
                    "acop": 51
                }
            ]
        },
        "pvs": {
            "acr": [
                {
                    "acor": ["CAdmin"],
                    "acop": 63
                }
            ]
        }
    }
}

try:
    response = requests.put(URL, headers=header, json=body)
    if response.status_code == 200:
        print("acp created.")
    else:
        print(f"acp not created. status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Error occurred: {e}")