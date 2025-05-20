#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  SensorData.py
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
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np
    scd = pd.read_csv('/home/kemkaa/scd30/scd30.csv')
    mq = pd.read_csv('/home/kemkaa/MQ137/mq137.csv')
    ph = pd.read_csv('/home/kemkaa/MQ137/pH.csv')
    scd = scd.set_index('Date')
    mq = mq.set_index('Date')
    ph = ph.set_index('Date')
    
    print(scd)
    print(mq)
    print(ph)
    mqT1 = mq
    
    #['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])
    #
#Trial 0: 04/01/25 - 04/08/25
#Classroom Control: 04/09/25 - 04/10/25
#House Control: 04/11/25 -04/12/25
#Trial 1: 04/13/25 - 04/21/25

    #Removed dates
    T0start_date = "04/01/25"
    T0end_date = "04/08/25"
    
    CCstart_date = "04/09/25"
    CCend_date = "04/10/25"
    
    HCstart_date = "04/11/25"
    HCend_date = "04/12/25"
    
    T1start_date = "04/13/25"
    T1end_date = "04/21/25"

    # Remove rows in the date range
    mqT0 = mq[mq.index.to_series().between(T0start_date, T0end_date)]
    print(mqT0)
    scdT0 = scd[scd.index.to_series().between(T0start_date, T0end_date)]
    print(mqT0)
    
    mqCC = mq[mq.index.to_series().between(CCstart_date, CCend_date)]
    scdCC = scd[scd.index.to_series().between(CCstart_date, CCend_date)]

    mqHC = mq[mq.index.to_series().between(HCstart_date, HCend_date)]
    scdHC = scd[scd.index.to_series().between(HCstart_date, HCend_date)]
    
    mqT1 = mq[mq.index.to_series().between(T1start_date, T1end_date)]
    scdT1 = scd[scd.index.to_series().between(T1start_date, T1end_date)]
    
    mqTime = mqT1['Time']
    mqVoltage = mqT1['Voltage(V)']
    plt.scatter(mqTime,mqVoltage,alpha=0.4,s=1)
    plt.title("Trial 1: Voltage v.s Time")
    plt.xlabel("Time")
    plt.ylabel("Voltage")
    plt.show()
    
    scdTime = scdT1['Time']
    scdCO2 = scdT1['CO2']
    plt.scatter(scdTime,scdCO2,alpha=0.4,s=1)
    plt.title("Trial 1: CO2 v.s Time")
    plt.xlabel("Time")
    plt.ylabel("CO2")
    plt.show()
    
    scdHum = scdT1['Humidity']
    plt.scatter(scdTime,scdHum,alpha=0.4,s=1)
    plt.title("Trial 1: Hum v.s Time")
    plt.xlabel("Time")
    plt.ylabel("Humidity")
    plt.show()
    
    scdTemp = scdT1['Temperature']
    plt.scatter(scdTime,scdTemp,alpha=0.4,s=1)
    plt.title("Trial 1: Temp v.s Time")
    plt.xlabel("Time")
    plt.ylabel("Temperature")
    plt.show()
    
    mqTime = mqHC['Time']
    mqVoltage = mqHC['Voltage(V)']
    plt.scatter(mqTime,mqVoltage,alpha=0.4,s=1)
    plt.title("House Control: Voltage v.s Time")
    plt.xlabel("Time")
    plt.ylabel("Voltage")
    plt.show()
    
    scdTime = scdHC['Time']
    scdCO2 = scdHC['CO2']
    plt.scatter(scdTime,scdCO2,alpha=0.4,s=1)
    plt.title("House Control: CO2 v.s Time")
    plt.xlabel("Time")
    plt.ylabel("CO2")
    plt.show()
    
    scdHum = scdHC['Humidity']
    plt.scatter(scdTime,scdHum,alpha=0.4,s=1)
    plt.title("House Control: Hum v.s Time")
    plt.xlabel("Time")
    plt.ylabel("Humidity")
    plt.show()
    
    scdTemp = scdHC['Temperature']
    plt.scatter(scdTime,scdTemp,alpha=0.4,s=1)
    plt.title("House Control: Temp v.s Time")
    plt.xlabel("Time")
    plt.ylabel("Temperature")
    plt.show()
    
    sys.exit(main(sys.argv))
