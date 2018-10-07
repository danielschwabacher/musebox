class SignalParser():
    '''
        SignalParser objects handle writing Serial data
        back to Arduino.
        Primarly, the write back data is used to
        update LED states.
    '''
    def __init__(self, serial_obj):
        self.serial = serial_obj
        self.valid_codes = [b'fd', b'3d', b'5d', b'4f']
        
    def is_valid(self, sig_code):
        if (sig_code in self.valid_codes):
            return True
        return False 
    
    
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
                Resets the music queue
            '''
            rv = 'v'
            return rv