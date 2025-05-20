import time
import board
import busio
import adafruit_sgp40
import adafruit_scd30
import os
if __name__ == '__main__':
    
    i2c = board.I2C()  # uses board.SCL and board.SDA
    # i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
    i2c = busio.I2C(board.SCL, board.SDA, frequency=50000)
    sgp = adafruit_sgp40.SGP40(i2c)

    scd = adafruit_scd30.SCD30(i2c)
    csv_file_sgp = '/home/kemkaa/sgp40/sgp40.csv'
    try:
        with open(csv_file_sgp, 'a+') as f:
            if os.stat(csv_file_sgp).st_size == 0:
                f.write('Date,Time,Real Gas(ppm),VOC(VOC index)\r\n')
    except Exception as e:
        print(f"Error opening file: {e}")
        exit(1)

    while True:
        temperature = scd.temperature
        humidity = scd.relative_humidity
        compensated_raw_gas = sgp.measure_raw(temperature = temperature, relative_humidity = humidity)
        voc_index = sgp.measure_index(temperature = temperature, relative_humidity = humidity)
        timestamp = time.strftime('%m/%d/%y'), time.strftime('%H:%M:%S')

        print(f"SGP40: {timestamp[0]},{timestamp[1]},{compensated_raw_gas} ppm,{voc_index} VOC\n")
        try:    
                with open(csv_file_sgp, 'a') as f:
                    timestamp = time.strftime('%m/%d/%y'), time.strftime('%H:%M:%S') 
                    f.write(f"{timestamp[0]},{timestamp[1]},{compensated_raw_gas},{voc_index}\r\n")
        except Exception as e:
            print(f"Error writing to file: {e}")
        else:
            print("Waiting for new data...")
            
        time.sleep(30)