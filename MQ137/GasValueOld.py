#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  GasValue.py
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
    import board
    import busio
    from adafruit_ads1x15.ads1115 import ADS1115
    from adafruit_ads1x15.analog_in import AnalogIn

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
    chan = AnalogIn(ads, 0)

    # 4. Loop to Read and Process Data
    while True:
        # Read voltage value from channel A0
        raw_adc = chan.value        # 16-bit ADC raw value
        voltage = chan.voltage      # Measured voltage in volts
        
        # Print raw ADC value and voltage
        print(f"Raw ADC Value: {raw_adc}")
        print(f"Voltage: {voltage:.4f} V")

   

    time.sleep(20)

    sys.exit(main(sys.argv))
