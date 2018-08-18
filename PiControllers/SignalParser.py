class SignalParser():
	'''
		SignalParser objects handle writing Serial data
		back to Arduino.
		Primarly, the write back data is used to
		update LED states.
	'''
	def __init__(self, serial_obj):
		self.serial = serial_obj
	
	def parse(self, signal_code):
		'''
			Figures out what to do with the raw byte 
			values
		'''
		if (signal_code == b'fd'):
			'''
				Represents the Start/Stop button 
				on the IR remote
			'''
			rv = 'p'
			self.serial.write('p')
			return rv
			
			
		if (signal_code == b'3d'):
			'''
				Represents the next button on 
				the IR remote_object_tree_item
			'''
			rv = 'n'
			self.serial.write('n')
			return rv

			
			
		if (signal_code == b'5d'):
			'''
				Represents the Power button on 
				the IR remote_object_tree_item
			'''
			rv = 'x'
			self.serial.write('x')
			return rv
