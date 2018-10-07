import binascii

class IRDecoder():
    def __init__(self):
        pass
        
    # Retuns a String representing the bytes
    # contained in the IR signal.
    def decode(self, bytes_to_decode, do_print):
        recieved_first_two_bytes = False
        decoded_resp = binascii.hexlify(bytes_to_decode)
        if (len(decoded_resp) == 2):
            recieved_first_two_bytes = True
        if (recieved_first_two_bytes):
            if (do_print):
                print("Bytes recieved: " + str(decoded_resp))
            return decoded_resp
        else:
            pass
