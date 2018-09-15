import RPi.GPIO as GPIO
import time



class LEDController():
	def __init__(self):
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BCM)
		self.PROCESS_PIN = 21
		self.ERROR_PIN = 19
		GPIO.setup(self.PROCESS_PIN, GPIO.OUT, initial=GPIO.LOW)
		GPIO.setup(self.ERROR_PIN, GPIO.OUT, initial=GPIO.LOW)
	def blink_processing_light(self):
		GPIO.output(self.PROCESS_PIN, GPIO.HIGH)
		time.sleep(1)
		GPIO.output(self.PROCESS_PIN, GPIO.LOW)

	def blink_error_light(self):
		GPIO.output(self.ERROR_PIN, GPIO.HIGH)
		time.sleep(1)
		GPIO.output(self.ERROR_PIN, GPIO.LOW)
