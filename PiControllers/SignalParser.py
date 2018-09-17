class SignalParser():
	'''
		SignalParser objects handle translating IR codes.
	'''
	def __init__(self, serial_obj):
		self.serial = serial_obj
		self.valid_codes = [b'fd', b'3d', b'5d', b'4f', b'9d', b'57', b'dd', b'1f']
		
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
		if (signal_code == b'fd'):
			'''
				Represents the Start/Stop button 
				on the IR remote
			'''
			rv = 'p'
			self.serial.write(b'p')
			return rv
			
			
		if (signal_code == b'3d'):
			'''
				Represents the next button on 
				the IR remote
			'''
			rv = 'n'
			self.serial.write(b'n')
			return rv

			
			
		if (signal_code == b'5d'):
			'''
				Represents the Power button on 
				the IR remote
			'''
			rv = 'x'
			self.serial.write(b'x')
			return rv
			
		if (signal_code == b'4f'):
			'''
				Represnt the ST/REPT button on
				the IR remote
				Resets the music queue.
				NOT USED
			'''
			rv = 'v'
			return rv
		
		if (signal_code == b'9d'):
			'''
				Represents the volume up 
				button on IR remote
			'''
			rv = 'u'
			return rv
			
		if (signal_code == b'57'):
			'''
				Represents the volume down button on 
				the IR remote
			'''
			rv = 'd'
			return rv
			
		if (signal_code == b'dd'):
			'''
			Represents the back/rewind button on
			the IR remote
			'''
			rv = 'r'
			return rv
			
		if (signal_code == b'1f'):
			'''
				Represents the down button on the IR remote
				Used to play previous song in queue.
			'''
			rv = 'b'
			return rv 
