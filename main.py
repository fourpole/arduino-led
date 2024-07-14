# TODO: Get temperature data from weather.gov API and display it
# TODO: Write serial data to USB port to turn on and off LED

import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(2)

while True:
    print('Enter Command: ', end="")
    led_state = input()
    print("input: ", led_state)
    ser.write(bytes(led_state + '\n', "utf-8"))
    # time.sleep(1)
    print('output: ', ser.readline().decode('utf-8'))