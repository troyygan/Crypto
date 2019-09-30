#!/usr/bin/python

from des import DesKey

key0 = DesKey("hsueo se") # FOR DES
key1 = DesKey("a key for TRIPLE") # for 3DES, same as "a key for TRIPLEa key for"
key2 = DesKey("a 24-byte key for TRIPLE") # for 3DES
key3 = DesKey("12345678REAL_KEY") # for DES, same as "REAL_KEY"

key0.is_single()
key1.is_triple()
key2.is_single()
key3.is_triple()

enc = key0.encrypt("any long message")

print enc
