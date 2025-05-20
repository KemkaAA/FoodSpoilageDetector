#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  scdlog.py
#  
#  Copyright 2025  <kemkaa@raspberrypi4>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


def main(args):
    return 0

if __name__ == '__main__':
    import sys
    import time
    import busio
    import adafruit_scd30
    import board
    import os

    # Initialize I2C bus and sensor
    i2c = busio.I2C(board.SCL, board.SDA, frequency=50000)
    scd = adafruit_scd30.SCD30(i2c)

    # Open the CSV file in append mode, and write headers if the file is empty
    csv_file_path = '/home/kemkaa/scd30/scd30.csv'
    try:
        with open(csv_file_path, 'a+') as f:
            if os.stat(csv_file_path).st_size == 0:
                f.write('Date,Time,Temperature (°C),CO2 (ppm),Humidity (%)\r\n')
    except Exception as e:
        print(f"Error opening file: {e}")
        exit(1)

    # Retry initialization in case the sensor is not ready immediately
    retry_attempts = 5
    for attempt in range(retry_attempts):
        if scd.data_available:
            print("Sensor initialized successfully.")
            break
        else:
            print(f"Attempt {attempt + 1}: Sensor not ready. Retrying...")
            time.sleep(2)
    else:
        print("Failed to initialize sensor after retries.")
        exit(1)

    # Continuously read and log data
    while True:
        if scd.data_available:
            # Read data from the sensor
            temperature = scd.temperature
            co2 = scd.CO2
            humidity = scd.relative_humidity
            
            # Log data to the CSV file
            try:
                with open(csv_file_path, 'a') as f:
                    timestamp = time.strftime('%m/%d/%y'), time.strftime('%H:%M')
                    f.write(f"{timestamp[0]},{timestamp[1]},{temperature:.2f},{co2},{humidity:.2f}\r\n")
                print(f"Logged data: {timestamp[0]} {timestamp[1]}, {temperature:.2f}°C, {co2} ppm, {humidity:.2f}%")
            except Exception as e:
                print(f"Error writing to file: {e}")
        
        else:
            print("Waiting for new data...")
        
        # Sleep for 30 seconds before reading again
        time.sleep(30)

    sys.exit(main(sys.argv))
