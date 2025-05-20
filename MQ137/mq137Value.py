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
    import math

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
    # Sensor-specific constants
    V_CIRCUIT = 5.0  # Supply voltage to the sensor (V)
    R_L = 10_000     # Load resistance in ohms (check datasheet for your specific setup)
    R0 = 1_000       # Clean air resistance (ohms, needs to be calibrated)

    # Calibration curve constants (based on datasheet graph for NH3)
    M = -1.5  # Slope of the line (approximation)
    B = 1.0   # Intercept (approximation)

    def calculate_rs(voltage):
        """
        Calculate sensor resistance Rs based on the measured voltage.
        :param voltage: Measured sensor output voltage.
        :return: Sensor resistance (Rs) in ohms.
        """
        if voltage == 0:  # Avoid division by zero
            return float('inf')
        return (V_CIRCUIT - voltage) * R_L / voltage

    def calculate_ppm(rs):
        """
        Calculate gas concentration (ppm) based on Rs and the calibration curve.
        :param rs: Sensor resistance (Rs) in ohms.
        :return: Gas concentration in ppm.
        """
        rs_ratio = rs / R0
        log_ppm = M * math.log10(rs_ratio) + B
        return 10 ** log_ppm

    # Main loop
    while True:
        voltage = chan.voltage
        print(f"Sensor Voltage: {voltage:.4f} V")

        # Calculate Rs
        rs = calculate_rs(voltage)
        print(f"Sensor Resistance (Rs): {rs:.2f} ohms")

        # Calculate gas concentration (ppm)
        ppm = calculate_ppm(rs)
        print(f"Gas Concentration: {ppm:.2f} ppm")

        time.sleep(2)

    sys.exit(main(sys.argv))
