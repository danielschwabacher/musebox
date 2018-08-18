import binascii

class IRDecoder():
	def __init__(self):
		pass
		
	# Retuns a String representing the bytes
	# contained in the IR signal.
	def decode(self, bytes_to_decode, do_print):
		decoded_resp = binascii.hexlify(bytes_to_decode)
		if (do_print):
			print("Bytes recieved: " + str(decoded_resp))
		return decoded_resp
