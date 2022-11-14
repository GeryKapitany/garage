import RPi.GPIO as GPIO
import time

#GPIO Mode
GPIO.setmode(GPIO.BCM)

#set GPIO Pins
GPIO_TRIGGER = 25
GPIO_ECHO = 24
#set GPIO Led Pins
LEDred=21
LEDyellow=20
LEDgreen=16

#set GPIO
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

GPIO.setup(LEDred, GPIO.OUT)
GPIO.setup(LEDyellow, GPIO.OUT)
GPIO.setup(LEDgreen, GPIO.OUT)

def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2

    return distance

def red():
    GPIO.output(LEDred, True)
    GPIO.output(LEDyellow, False)
    GPIO.output(LEDgreen, False)
def yellow():
    GPIO.output(LEDred, False)
    GPIO.output(LEDyellow, True)
    GPIO.output(LEDgreen, False)
def green():
    GPIO.output(LEDred, False)
    GPIO.output(LEDyellow, False)
    GPIO.output(LEDgreen, True)


if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print ("Distance = %.1f cm" % dist)
            if dist >= 50:
                red()
            if 50 > dist > 20:
                yellow()
            if dist <= 20:
                green()
            time.sleep(1)

        # Exit by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped...")
        GPIO.cleanup()
