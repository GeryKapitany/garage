# Module Imports
import mariadb
import sys
import Adafruit_DHT
import time
import datetime

# Set GPIO
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 23

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="garage",
        password="garage2022",
        host="192.168.1.112",
        port=3306,
        database="garage"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()

while True:
    # Readin from sensor 
    now = datetime.datetime.utcnow()    
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        #print("Temp={0:0.0f}°C Humidity={1:0.0f}%".format(temperature, humidity))

        # Insert into DB    
        try: 
            cur.execute("INSERT INTO temp (date,temperature,humidity) VALUES (?, ?, ?)", (now.strftime('%Y-%m-%dT%H:%M:%S'),temperature,humidity))
        except mariadb.Error as e: 
            print(f"Error: {e}")
        conn.commit()

    #else:
        #print("Sensor failure. Check wiring.");

    time.sleep(3);
    
conn.close()