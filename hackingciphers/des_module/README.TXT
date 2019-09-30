###This module is for DES

##Installation

pip install des


###NOTES

- import DesKey from des module
ex: 
from des import DesKey
   
- Need to create the object first which is a key of module des
- For python 3, you need to convert the plaintext to bytes by adding 'b' as a prefix.
- Also, Des key is only divisible by 8 bytes... You can create 8, 16(2DES), or 24(3DES) byte key
ex: 
key0 = DesKey(b"some key") #8 byte key
key1 = DesKey(b"a key for TRIPLE") #for 3DES, same as "a key for TRIPLEa key fo"
key2 = DesKEy(b"a 24-byte key for TRIPLE") #for 3DES
key3 = DesKey(b"1234567812345678REAL_KEY") #for DES, same as REAL_KEY"

- For python 2, no need to convert the plaintext to bytes. Just omit the prefix 'b'

- DES algorithm requires the message to be of any length that is a multiple of 8. By default


###Encryption

- Use the object key created above and method 'encrypt' to perform encryption
- For python 3 you still need convert the plaintext to bytes.
- For python 2, no need to convert the message to bytes

ex:

key0.encrypt(b"any long message")

###Decryption

key0.decrypt(b"encrypted message")


###MODE

- by default, des module uses ECB mode
- To enable the CBC mode, you need to add an arguement 'initial', as the initial value. The arguements may be either a bytes object of length 8 \
or an integer using big-endian.

ex:
key0.encrypt(b"any long message", initial=0)
#or
key0.encrypt(b"any long message", initial=b"\0"*8) #they will have the same output from the first one above

###PADDING (OPTIONAL) 

- You can enable PKCS5 Padding Mode(by passing the arguement padding with a TRUTHY value).

ex:
key0.encrypt(b"abc", padding=True) 

- To decrypt with PKCS5 
ex:
key0.decrypt(b"09^5123*&@&^$", padding=True)


