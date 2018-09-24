import json
import os

class SignalParser():
	'''
		SignalParser objects handle translating IR codes.
	'''
	def __init__(self, serial_obj):
		self.serial = serial_obj
		self.prop_file = "led_remote.json"
		self.properties_file_location = os.path.expanduser("~") + "/IrProperties/" + self.prop_file
		self.valid_codes = []
		self.lookup_map = {}
		self.get_codes()
		
		
	def get_codes(self):
		with open(self.properties_file_location) as properties:
			data = json.loads(properties.read())
			for key, val in data.items():
				self.valid_codes.append(val)
				self.lookup_map[val] = key
			
	def is_valid(self, sig_code):
		if (sig_code in self.valid_codes):
			return True
		return False 
	
	
	def parse(self, signal_code):
		'''
			Figures out what to do with the raw byte 
			values
			
			If a valid code is recieved, a single character 
			is returned which represents the action to perform. 
			
			This is essentially a lookup table which maps:
			IR bytes -> Action characters
		'''
		if (signal_code in self.valid_codes):
			try:
				action = self.lookup_map[signal_code]
				print("action is: " + action)
				if (action == "power"):
					rv = 'x'
					self.serial.write(b'x')
					return rv
				if (action == "start_stop"):
					rv = 'p'
					self.serial.write(b'p')
					return rv
				if (action == "next_song"):
					rv = 'n'
					self.serial.write(b'n')
					return rv		
				if (action == "volume_up"):
					rv = 'u'
					return rv
				if (action == "volume_down"):
					rv = 'd'
					return rv
				if (action == "rewind"):
					rv = 'r'
					return rv				
				if (action == "previous_song"):
					rv = 'b'
					return rv
			except KeyError:
				print("Key not found")
				return '0'
		else:
			print("Code not found in valid codes.")
			return '0'
		
