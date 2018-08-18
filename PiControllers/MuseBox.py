import serial
import RPi.GPIO as GPIO
import time
from MusicController import MusicController
from SignalParser import SignalParser
from IRDecoder import IRDecoder

ser=serial.Serial("/dev/ttyACM0", 28800, timeout=0.05);
time.sleep(1)
ser.baudrate=28800;
VERSION = "0.0.1"
print("Running MuseBox, version: " + VERSION + "...");

GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(11, GPIO.OUT)

class MuseBox():
	def __init__(self):
		self.power = True
		self.decoder = IRDecoder()
		self.parser = SignalParser(ser)
		self.controller = MusicController()
	
	def toggle_power(self):
		self.power = not self.power
		exit(1)
	
	def process_loop(self):
		while (self.power):
			serial_line_result = ser.read_until(b'70')
			ser.flushInput()
			sig_recv = self.decoder.decode(serial_line_result, True)
			parse_result = self.parser.parse(sig_recv)
			if (parse_result == 'p'):
				self.controller.toggle_start_stop()
			if (parse_result == 'n'):
				self.controller.play_new_song()
			elif (parse_result == 'x'):
				self.toggle_power()
			time.sleep(2)
				
box1 = MuseBox()
box1.process_loop()

