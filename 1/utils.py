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

def fixed_XOR(a,b):
    return "".join([ "%x" % (int(x,16) ^ int(y,16)) for (x,y) in zip(a,b)])
