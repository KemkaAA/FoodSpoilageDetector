# SPDX-FileCopyrightText: 2020 by Bryan Siepert for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense
import time
import board
import busio
import adafruit_sgp40
import adafruit_scd30

# If you have a temperature sensor, like the bme280, import that here as well
# import adafruit_bme280
if __name__ == '__main__':
    i2c = board.I2C()  # uses board.SCL and board.SDA
    # i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
    i2c = busio.I2C(board.SCL, board.SDA, frequency=50000)
    sgp = adafruit_sgp40.SGP40(i2c)

    scd = adafruit_scd30.SCD30(i2c)
    # And if you have a temp/humidity sensor, define the sensor here as well
    # bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

    while True:

        # Lets quickly grab the humidity and temperature
        temperature = scd.temperature
        humidity = scd.relative_humidity
        
        compensated_raw_gas = sgp.measure_raw(temperature = temperature, relative_humidity = humidity)
        voc_index = sgp.measure_index(temperature = temperature, relative_humidity = humidity)
        print("Raw Gas: ", compensated_raw_gas)
        
        print("VOC Index:", voc_index)
        
        print("")
        time.sleep(1)
