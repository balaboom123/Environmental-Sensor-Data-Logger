import serial
import csv

# 設定 Arduino 串口 (確認你的 Arduino 是哪個 COM 口，例如 'COM3' 或 '/dev/ttyUSB0')
ser = serial.Serial('COM5', 9600, timeout=1)

# 開啟 CSV 檔案
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(['date', 'time', 'pm25', 'co', 'co2', 'tvoc'])  # CSV 標題

    while True:
        try:
            # 讀取串列資料
            line = ser.readline().decode().strip().split(",")
            data = line

            # 嘗試轉換類型
            date, time, pm25, co, co2, tvoc = data
            pm25 = float(pm25)  # 轉換 PM2.5
            co = float(co)      # 轉換 CO
            co2 = int(co2)      # 轉換 CO2
            tvoc = int(tvoc)    # 轉換 TVOC

            # 如果成功轉換，則印出並寫入 CSV
            print([date, time, pm25, co, co2, tvoc])
            writer.writerow([date, time, pm25, co, co2, tvoc])

        except ValueError:
            print("⚠️ ignore:", line)
