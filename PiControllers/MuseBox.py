import serial
import RPi.GPIO as GPIO
import time
from MusicController import MusicController
from SignalParser import SignalParser
from IRDecoder import IRDecoder
from LEDController import LEDController
import pygame
import random
import os
ser=serial.Serial("/dev/ttyACM0", 28800, timeout=0.05);
time.sleep(1)
ser.baudrate=28800;
VERSION = "0.0.1"

print("Running MuseBox, version: " + VERSION + "...");


NEXT_SONG = pygame.USEREVENT + 1

# We need this in order to use in a headless (no monitor) environment
os.environ["SDL_VIDEODRIVER"] = "dummy"

class MuseBox():
	def __init__(self):
		pygame.init()
		self.power = True
		self.decoder = IRDecoder()
		self.parser = SignalParser(ser)
		self.music_controller = MusicController()
		self.led_controller = LEDController()
		self.music_controller.initialize()
	
	def toggle_power(self):
		if (self.power):
			# turn off if power is on
			self.music_controller.reset()
			self.led_controller.toggle_power_off_light(0)
		else:
			# turn on if power is off
			self.music_controller.initialize()
			self.led_controller.toggle_power_off_light(1)
		self.power = not self.power
		# wait and poll forever until power is restored
		while (not self.power):
			if (ser.inWaiting()):
				serial_line_result = ser.read_until(b'70')
				ser.flushInput()
				sig_recv = self.decoder.decode(serial_line_result, True)
				parse_result = self.parser.parse(sig_recv)
				if (parse_result == 'x'):
					self.led_controller.blink_processing_light()
					self.toggle_power()
	
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
						self.music_controller.toggle()
					elif (parse_result == 'n'):
						self.led_controller.blink_processing_light()
						self.music_controller.next_song()
					elif (parse_result == 'x'):
						self.led_controller.blink_processing_light()
						self.toggle_power()
					elif (parse_result == 'u'):
						# volume up
						self.led_controller.blink_processing_light()
						self.music_controller.volume_up()
						pass
					elif (parse_result == 'd'):
						# volume down
						self.led_controller.blink_processing_light()
						self.music_controller.volume_down()
						pass
					elif (parse_result == 'r'):
						# rewind/back button
						self.led_controller.blink_processing_light()
						self.music_controller.rewind_current_song()
					elif (parse_result == 'b'):
						self.led_controller.blink_processing_light()
						self.music_controller.previous_song()
				else:
					# Invalid code, show error
					self.led_controller.blink_error_light()
			for event in pygame.event.get():
				if event.type == NEXT_SONG:
					self.music_controller.next_song()
					# pygame.mixer.music.play()
				
box1 = MuseBox()
box1.process_loop()

