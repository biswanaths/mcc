from binascii import (
    a2b_base64,
    b2a_base64,
    hexlify,
    unhexlify
)

def hex2base64(input):
    return b2a_base64(unhexlify(input))
   
   
def base642hex(input):
    return hexlify(a2b_base64(input)) 
