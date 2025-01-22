# Smart Buoy (Client)  
**oneM2M Application Entity**

This project contains the client code for the **Smart Buoy**.  
The system utilizes the following sensors to gather wave-related data:
- **Accelerometer**: Measures wave motion.
- **Ultrasonic Sensor**: Calculates wave height.
- **GPS Sensor**: Provides location information.
- **Temperature Sensor**: Records sea surface temperature (SST).

Collected data includes:  
**Wave Period**, **Wave Height**, **Location**, and **Sea Surface Temperature**.

---

## 🚀 How to Run

1. **Configure the Settings**  
   Open the `config.ini` file and set the necessary parameters.

2. **Run the Application**  
   Execute the following command in your terminal:  
   ```bash
   python main.py
   ```

---

## 📂 File Structure
```
.
├── main.py           # Main script to run the client
├── config.ini        # Configuration file
├── sensors/          # Sensor-related modules
├── utils/            # Utility functions
└── logs/             # Logs for mock simulation
```

---