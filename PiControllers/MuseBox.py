import serial
import RPi.GPIO as GPIO
import time
from MusicController import MusicController
from SignalParser import SignalParser
from IRDecoder import IRDecoder
from LEDController import LEDController

ser=serial.Serial("/dev/ttyACM0", 28800, timeout=0.05);
time.sleep(1)
ser.baudrate=28800;
VERSION = "0.0.1"

print("Running MuseBox, version: " + VERSION + "...");

class MuseBox():
	def __init__(self):
		self.power = True
		self.decoder = IRDecoder()
		self.parser = SignalParser(ser)
		self.music_controller = MusicController()
		self.led_controller = LEDController()
		self.music_controller.reset()
	
	def toggle_power(self):
		self.power = not self.power
		exit(1)

	def process_loop(self):
		while (self.power):
			if (ser.inWaiting()):
				serial_line_result = ser.read_until(b'70')
				ser.flushInput()
				sig_recv = self.decoder.decode(serial_line_result, True)
				if (self.parser.is_valid(sig_recv)):
					parse_result = self.parser.parse(sig_recv)
					if (parse_result == 'p'):
						self.led_controller.blink_processing_light()
						self.music_controller.toggle_start_stop()
					elif (parse_result == 'n'):
						self.led_controller.blink_processing_light()
						self.music_controller.play_new_song()
					elif (parse_result == 'x'):
						self.led_controller.blink_processing_light()
						self.toggle_power()
					elif (parse_result == 'v'):
						self.led_controller.blink_processing_light()
						self.music_controller.clear_queue()
				else:
					self.led_controller.blink_error_light()
			time.sleep(2)
				
box1 = MuseBox()
box1.process_loop()

