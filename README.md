# Environmental Sensor Data Logger

This project demonstrates how to build a simple environmental data logger using an Arduino (e.g. Mega 2560), several gas/dust sensors and a real-time clock. Data are:

- **PM₂.₅** (dust)  
- **CO** (carbon monoxide)  
- **CO₂** & **TVOC** (total volatile organic compounds)  
- **Timestamp** from a DS1302 RTC  
- **Persistent storage** in EEPROM  
- **Serial output** for live monitoring  
- **CSV export** via a Python script

---

## Table of Contents

1. [Hardware & Wiring](#Hardware-&-Wiring)
2. [Software Requirements](#software-requirements)  

---

## Hardware & Wiring

| Sensor / Module            | Interface   | Connections                                                                 | Notes                                                       |
|----------------------------|-------------|-----------------------------------------------------------------------------|-------------------------------------------------------------|
| **DS1302 RTC**             | ThreeWire   | DAT → D9<br>CLK → D10<br>RST → D8<br>VCC → 5 V<br>GND → GND                  | —                                                           |
| **GP2Y1010AU0F (PM₂.₅)**   | Analog      | LED → D2 (via 150 Ω resistor)<br>VO → A1 (0.1 µF cap to GND)<br>VCC → 5 V<br>GND → GND | Pulsed-LED sampling; convert analog voltage to µg/m³        |
| **MQ-7 (CO sensor)**       | Analog      | Analog out → A0<br>VCC → 5 V<br>GND → GND                                   | May require heat-cycle for best accuracy                    |
| **CCS811 (CO₂ & TVOC)**    | I²C         | SDA → A4<br>SCL → A5<br>VCC → 3.3 V<br>GND → GND                             | Use Wire library; warm-up required before data ready        |
| **EEPROM**                 | On-board    | —                                                                           | 1–4 KB depending on Arduino model; used for ring-buffer log |

## How to Use

1. **Upload & Run Arduino**  
   - Wire up modules as per the wiring diagram.  
   - Open `sketch_mar19a.ino` in Arduino IDE, install libraries, select board & port, then click **Upload**.  
   - Open **Serial Monitor** (9600 baud) to see live CSV output.

2. **Log to CSV with Python**  
   - Ensure Python ≥ 3 and `pyserial` are installed:  

     ```bash
     pip install pyserial
     ```  

   - Edit `data_to_csv.py` to point at your serial port.  
   - Run:  

     ```bash
     python data_to_csv.py
     ```  

   - A `data.csv` file will appear in the same folder, containing timestamped PM₂.₅, CO, CO₂, and TVOC readings.

3. **Retrieve EEPROM Records (Optional)**  
   - Use a separate Arduino sketch or Serial dump tool to read and decode the raw EEPROM entries if you need to recover data when the device was offline.

## Software Requirements

- **Arduino IDE** (≥ 1.8.x)  
- **Libraries** (install via Library Manager):  
  - `ThreeWire`  
  - `RtcDS1302`  
  - `Adafruit_CCS811`  
- **Python 3** with:  

  ```bash
  pip install pyserial
