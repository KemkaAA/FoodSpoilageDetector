#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  scdLogger.py
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
    import os
    import time
    import busio
    import adafruit_scd30
    import board

    i2c = busio.I2C(board.SCL, board.SDA, frequency=50000)
    scd = adafruit_scd30.SCD30(i2c)

    try:
        f = open('/home/kemkaa/scd30/scd30.csv', 'a+')
        if os.stat('/home/kemkaa/scd30/scd30.csv').st_size == 0:
                f.write('Date,Time,Temperature,CO2,Humidity\r\n')
    except Exception as e:
        print(f"Error openning file:{e}")
        pass

    while True:
        if scd.data_available:
            f.write(f'{time.strftime("%m/%d/%y")},{time.strftime("%H:%M")},{scd.temperature:0.2f}C,{scd.CO2},{scd.relative_humidity:0.2f}%\r\n')

            #f.write('{0},{1},{2:0.2f}*C,{3:0.2f}PPM,{4:0.2f}%\r\n'.format(
                #time.strftime('%m/%d/%y'),
                #time.strftime('%H:%M'),
               # scd.temperature,
              #  scd.CO2,
             #   scd.relative_humidity))
            
            print("Data Available!")
            print("CO2: %d PPM" % scd.CO2)
            print("Temperature: %0.2f degrees C" % scd.temperature)
            print("Humidity: %0.2f %% rH" % scd.relative_humidity)
            print("")
            print("Waiting for new data...")
            print("")
            
            f.write('{0},{1},{2:0.2f}*C,{3:0.2f}PPM,{4:0.2f}%\r\n'.format(
                time.strftime('%m/%d/%y'),
                time.strftime('%H:%M'),
                scd.temperature,
                scd.CO2,
                scd.relative_humidity))

        time.sleep(30)
        
    sys.exit(main(sys.argv))
