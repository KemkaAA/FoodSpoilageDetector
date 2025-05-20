#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  phValue.py
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

# To- Do
def main(args):
    return 0

if __name__ == '__main__':
    import sys
    import time
    import board
    import busio
    from adafruit_ads1x15.ads1115 import ADS1115
    from adafruit_ads1x15.analog_in import AnalogIn
    import math
    import os

    # 1. I²C Setup
    # Create an I²C bus instance
    i2c = busio.I2C(board.SCL, board.SDA)

    # 2. ADS1115 Initialization
    # Create an ADS1115 ADC instance
    ads = ADS1115(i2c)

    # Set gain for voltage range:
    # Gain=1 (default) means +/- 4.096V range
    ads.gain = 1

    # 3. Create a Channel to Read Analog Data
    # Use channel A0 for the MQ-137 sensor
    chan = AnalogIn(ads, 1)
    
    csv_file_path = '/home/kemkaa/MQ137/pH.csv'
    try:
        with open(csv_file_path, 'a+') as f:
            if os.stat(csv_file_path).st_size == 0:
                f.write('Date,Time,pH,Voltage(V),Resistance Voltage(rs)\r\n')
    except Exception as e:
        print(f"Error opening file: {e}")
        exit(1)
        
    def voltage_to_pH(voltage):
        # Calibration values (this may vary depending on your sensor)
        V_offset = 2.5  # Voltage at pH 7 (can vary with sensor calibrate with known value)
        slope = 0.059  # mV per pH unit, typical for many sensors (0.05916 V/pH)

        # Convert voltage to pH
        pH = (voltage - V_offset) / slope
        return pH

    # Example usage
    #while True:
     #   voltage = read_pH_voltage()
      #  pH_value = voltage_to_pH(voltage)
        print("pH: {:.2f}".format(pH_value))
        time.sleep(1)

    while True:
        if chan.voltage > 0:
            voltage = chan.voltage
            pH_value = voltage_to_pH(voltage)
            raw_adc = chan.value
        
            print(f"pH: {pH_value}")
            print(f"Raw ADC Value: {raw_adc}")
            print(f"Voltage: {voltage:.4f} V")
            try:    
                with open(csv_file_path, 'a') as f:
                    timestamp = time.strftime('%m/%d/%y'), time.strftime('%H:%M:%S') 
                    f.write(f"{timestamp[0]},{timestamp[1]},{pH_value},{voltage:.4f},{raw_adc:.2f}\r\n")
                print(f"Logged data: {timestamp[0]}, {timestamp[1]}, {pH_value}pH, {voltage:.4f}V, {raw_adc:.2f}")
            except Exception as e:
                print(f"Error writing to file: {e}")
            
        else:
            print("Waiting for new data...")
        time.sleep(30)

    
    sys.exit(main(sys.argv))
