# Smart Buoy (Client)
**oneM2M Application Entity**

This project contains the client code for the **Smart Buoy**.
It collects real-time wave data using multiple sensors:

- **Accelerometer**: Measures wave motion (used to estimate wave period).
- **Ultrasonic Sensor**: Calculates wave height.
- **GPS Sensor**: Provides location information.
- **Temperature Sensor**: Records sea surface temperature (SST).

Collected data includes:
**Wave Period**, **Wave Height**, **Location**, and **Sea Surface Temperature**.

---

## 🚀 How to Run

1. **Configure the Settings**  
   Open the `config.ini` file and adjust the parameters under the following sections:
   - `CSE SERVER`: Set the IP, port, and CSE base for the oneM2M server.
   - `BUOY`: Specify the buoy name and mock mode.
   - `SENSORS`: Enable or disable individual sensors.

2. **Install Dependencies**  
   Make sure you have Python 3.x installed.  
   You may also need `requests` and other libraries:
   ```bash
   pip install requests
   ```

3. **Run the Application**  
   Execute:
   ```bash
   python main.py
   ```
   This will:
   - Check and register the AE (Smart Buoy) in the oneM2M CSE server.
   - Create necessary Containers for each active sensor.
   - Collect sensor data periodically and create CIN resources on the CSE server.

---

## 📂 File Structure

```
.
├── main.py            # Main script to run the client
├── config.ini         # Configuration file
├── sensors/
│   ├── mock_data.py   # Mock sensor data generation
│   └── sensors.py     # Real sensor data
├── utils/
│   ├── init.py        # Reads config and sets up objects
│   ├── oneM2M.py      # oneM2M-related API functions
│   └── setACP.py      # Create acp for TinyIoT
└── README.md
```

---

## 📌 Notes
- If `mock` is set to `TRUE` in `config.ini`, the client uses **mock sensor data**.
- If you have real sensors, implement and enable the `real_sensors.py` accordingly.
- Make sure the **oneM2M CSE server** (e.g., TinyIoT) is running before starting the client.
