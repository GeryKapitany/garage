# Module Imports
import mariadb
import sys
import Adafruit_DHT
import time
import datetime
from secrets import mariadb_pass

# Set GPIO
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 23

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="garage",
        password=mariadb_pass,
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

        # Insert into DB
        try:
            cur.execute("INSERT INTO temp (date,temperature,humidity) VALUES (?, ?, ?)", (now.strftime('%Y-%m-%dT%H:%M:%S'),temperature,humidity))
        except mariadb.Error as e:
            print(f"Error: {e}")
        conn.commit()

    time.sleep(3);

conn.close()
