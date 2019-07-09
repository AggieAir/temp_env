#!/usr/bin/python3
import fake_board
import digitalio
import busio
import time
import adafruit_bme280

import csv

# Create library object using our Bus I2C port
i2c = busio.I2C(fake_board.SCL, fake_board.SDA)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

# change this to match the location's pressure (hPa) at sea level
bme280.sea_level_pressure = 1013.25

#create csv file
with open('data.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    
    filewriter.writerow(['Time','Temperature','Humidity','Pressure'])
    #filewriter.writerow(['Temperature','Humidity','Pressure','Altitude',])

    startTime = time.time()

    while True:

        #obtains current values
        currentTime = time.time() - startTime
        currentTemp = bme280.temperature
        currentHumidity = bme280.humidity
        currentPressure = bme280.pressure
       # currentAlt = bme280.altitude

        #print to console temperature, humidity, pressure, altitude

        print("\nTime: %.1f seconds" % currentTime )
        print("Temperature: %0.1f C" % currentTemp)
        print("Humidity: %0.1f %%" % currentHumidity)
        print("Pressure: %0.1f hPa" % currentPressure)
        #print("Altitude = %0.2f meters" % currentAlt)
        

        #save to csv the data
        filewriter.writerow([currentTime,currentTemp, currentHumidity, currentPressure])

        time.sleep(.5)
