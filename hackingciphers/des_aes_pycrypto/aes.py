#!/usr/bin/python

import os
import random
from Crypto.Cipher import AES
import base64

key = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
print 'key is: ', [x for x in key]


###Initialization Vector is a requirement for AES enc/dec

iv = ''.join([chr(random.randint(0, 0xFF)) for i in range(16)])



###Encrypt with pycrypto module

aes = AES.new(key, AES.MODE_CBC, iv)
data= 'hello world 1234' # this is a 16 bytes data
encd = aes.encrypt(data)

print 'Encrypted data is: ', encd


