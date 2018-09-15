import RPi.GPIO as GPIO
import time



class LEDController():
	def __init__(self):
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BCM)
		self.PROCESS_PIN = 21
		self.ERROR_PIN = 19
		self.PLAYING_PIN = 20
		self.PAUSED_PIN = 16
		self.all_pins = [self.PROCESS_PIN, self.ERROR_PIN, self.PLAYING_PIN, self.PAUSED_PIN]
		GPIO.setup(self.PROCESS_PIN, GPIO.OUT, initial=GPIO.LOW)
		GPIO.setup(self.ERROR_PIN, GPIO.OUT, initial=GPIO.LOW)
		GPIO.setup(self.PLAYING_PIN, GPIO.OUT, initial=GPIO.LOW)
		GPIO.setup(self.PAUSED_PIN, GPIO.OUT, initial=GPIO.LOW)
	
	def blink_processing_light(self):
		GPIO.output(self.PROCESS_PIN, GPIO.HIGH)
		time.sleep(1)
		GPIO.output(self.PROCESS_PIN, GPIO.LOW)

	def blink_error_light(self):
		GPIO.output(self.ERROR_PIN, GPIO.HIGH)
		time.sleep(1)
		GPIO.output(self.ERROR_PIN, GPIO.LOW)

	def playing(self):
		GPIO.output(self.PLAYING_PIN, GPIO.HIGH)
		GPIO.output(self.PAUSED_PIN, GPIO.LOW)
	
	def paused(self):
		GPIO.output(self.PLAYING_PIN, GPIO.LOW)
		GPIO.output(self.PAUSED_PIN, GPIO.HIGH)
	
	def turn_off_all_lights(self):
		for pin in self.all_pins:
			GPIO.output(pin, GPIO.LOW)
			
	def toggle_power_off_light(self, power_state):
		'''
			If the power is off, turn on a light which indicates
			this. While the power is off, MuseBox won't respond to 
			IR codes, so an indicator is helpful.
			power_state is 0 if the power is off (light will be on)
			power_state is 1 if power is on (light will be off)
		'''
		if (not power_state):
			GPIO.output(self.ERROR_PIN, GPIO.HIGH)
		else:
			GPIO.output(self.ERROR_PIN, GPIO.LOW)

