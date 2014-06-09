import os
import dynamixel
import sys
import time
import serial
import pythonosc
import threading
import random

# code variables
codeVersion = "0.0.1"

# arduino variables
arduinoPortName = "/dev/tty.usbmodem141141"
arduinoBaudRate = 9600

# dynamixel variables
dynamixelPortName = "/dev/tty.usbserial-A9ITX7RZ"
dynamixelBaudRate = 1000000
dynamixelHighestServoId = 4






print "Beginning program version " + str(codeVersion) + "."


# connect to arduino
ser = serial.Serial(arduinoPortName, arduinoBaudRate)
print "Serial connection initialized with Arduino at serial port " + arduinoPortName + "."


# connect to dynamixel
dynamixelSerial = dynamixel.SerialStream(port=dynamixelPortName, baudrate=dynamixelBaudRate, timeout=1)
print "Serial connection initialized with USB2Dynamixel at serial port " + dynamixelPortName + "."
dynamixelNet = dynamixel.DynamixelNetwork(dynamixelSerial)
print "Scanning for Dynamixels..."
dynamixelNet.scan(1, dynamixelHighestServoId)

dynamixelActuators = []
for dyn in dynamixelNet.get_dynamixels():
	print "Dynamixel found with ID " + str(dyn.id)
	dynamixelActuators.append(dynamixelNet[dyn.id])

if not dynamixelActuators:
	print 'No Dynamixels Found!'
	sys.exit(0)
else:
	print "...Done"

for actuator in dynamixelActuators:
	actuator.moving_speed = 100
	actuator.synchronized = True
	actuator.torque_enable = True
	actuator.torque_limit = 800
	actuator.max_torque = 800



while True:
	char = raw_input("char to send to Arduino: ")
	ser.write(str(char)) # Convert the decimal number to ASCII then send it to the Arduino
	print "The character " + str(char) + " has been sent to Arduino."


	for actuator in dynamixelActuators:
		actuator.goal_position = int(raw_input("Position to go to? "))
	dynamixelNet.synchronize()
	for actuator in dynamixelActuators:
		actuator.read_all()
		time.sleep(0.01)
	for actuator in dynamixelActuators:
		print str(actuator._id) + "\t" + str(actuator.current_position)
	time.sleep(1)







































