#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  untitled.py
#  
#  Copyright 2024  <kemkaa@raspberrypi4>
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
    # SPDX-License-Identifier: Unlicense
    import sys
    import time
    import board
    import busio
    import adafruit_scd30
    import I2C_LCD_driver
    
     
    
    mylcd = I2C_LCD_driver.lcd()
    
    # SCD-30 has tempremental I2C with clock stretching, datasheet recommends
    # starting at 50KHz
    i2c = busio.I2C(board.SCL, board.SDA, frequency=50000)
    scd = adafruit_scd30.SCD30(i2c)

    while True:
        # since the measurement interval is long (2+ seconds) we check for new data before reading
        # the values, to ensure current readings.
        if scd.data_available:
            temperature = scd.temperature
            co2 = scd.CO2
            humidity = scd.relative_humidity
            
            
            print("Data Available!")
            print("CO2: %d PPM" % scd.CO2)
            print("Temperature: %0.2f degrees C" % scd.temperature)
            print("Humidity: %0.2f %% rH" % scd.relative_humidity)
            print("")
            print("Waiting for new data...")
            print("")
            
            mylcd.lcd_clear()
            mylcd.lcd_display_string("CO2:%d Hum:%0.2f" % (co2,humidity),1)
            mylcd.lcd_display_string("Tem:%0.2f" % temperature,2)
            
        time.sleep(5)
    
    sys.exit(main(sys.argv))
