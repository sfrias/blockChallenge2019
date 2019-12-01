# import libraries
import hashlib
import random
import string
import json
import binascii
import logging
import datetime
import collections
# following imports are required by PKI
import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

self._private_key = RSA.generate(2048, random)
self._public_key = self._private_key.publickey()
@property
   def identity(self):
      return
binascii.hexlify(self._public_key.exportKey(format='DER'))
.decode('ascii')
class Client:
   def __init__(self):
      random = Crypto.Random.new().read
      self._private_key = RSA.generate(1024, random)
      self._public_key = self._private_key.publickey()
      self._signer = PKCS1_v1_5.new(self._private_key)

   @property
   def identity(self)
      return

binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')

Familia1 = Client()
print (Familia1.identity)

def __init__(self, sender, recipient, value):
   self.sender = sender
   self.recipient = recipient
   self.value = value
   self.time = datetime.datetime.now()

if self.sender == "Genesis":
   identity = "Genesis"
else:
   identity = self.sender.identity


return collections.OrderedDict({
   'sender': identity,
   'recipient': self.recipient,
   'value': self.value,
   'time' : self.time})

def to_dict(self):
   if self.sender == "Genesis":
      identity = "Genesis"
   else:
      identity = self.sender.identity

   return collections.OrderedDict({
      'sender': identity,
      'recipient': self.recipient,
      'value': self.value,
      'time' : self.time})

def sign_transaction(self):
   private_key = self.sender._private_key
   signer = PKCS1_v1_5.new(private_key)
   h = SHA.new(str(self.to_dict()).encode('utf8'))
   return binascii.hexlify(signer.sign(h)).decode('ascii')

Familia1 = Client()
WasteCollect1 = Client()

t = Transaction(
   Dinesh,
   Ramesh.identity,
   5.0
)
signature = t.sign_transaction()
print (signature) 

def display_transaction(transaction):
   #for transaction in transactions:
   dict = transaction.to_dict()
   print ("sender: " + dict['sender'])
   print ('-----')
   print ("recipient: " + dict['recipient'])
   print ('-----')
   print ("value: " + str(dict['value']))
   print ('-----')
   print ("time: " + str(dict['time']))
   print ('-----')

transactions = []

Familia1 = Client()
Familia2  = Client()
WasteCollect1 = Client()
WasteCollect2 = Client()

t1 = Transaction(
   Familia1,
   WasteCollect2.identity,
   15.0
)


t1.sign_transaction()
transactions.append(t1)

t2 = Transaction(
   Familia1,
   WasteCollect1.identity,
   6.0
)
t2.sign_transaction()
transactions.append(t2)
t3 = Transaction(
   Familia2,
   WasteCollect2.identity,
   2.0
)
t3.sign_transaction()
transactions.append(t3)
t4 = Transaction(
   WasteCollect1,
   WasteCollect2.identity,
   4.0
)
t4.sign_transaction()
transactions.append(t4)
t5 = Transaction(
   Familia1,
   Familia2.identity,
   7.0
)
t5.sign_transaction()
transactions.append(t5)
t6 = Transaction(
   Familia2,
   WasteCollect1.identity,
   3.0
)
t6.sign_transaction()
transactions.append(t6)
t7 = Transaction(
   Familia1,
   Familia2.identity,
   8.0
)
t7.sign_transaction()
transactions.append(t7)
t8 = Transaction(
   WasteCollect1,
   WasteCollect2.identity,
   1.0
)
t8.sign_transaction()
transactions.append(t8)
t9 = Transaction(
   Familia1,
   WasteCollect2.identity,
   5.0
)
t9.sign_transaction()
transactions.append(t9)
t10 = Transaction(
   Familia1,
   WasteCollect1.identity,
   3.0
)
t10.sign_transaction()
transactions.append(t10)

for transaction in transactions:
   display_transaction (transaction)
   print ('--------------')

self.verified_transactions = []

self.previous_block_hash = ""

self.Nonce = ""

class Block:
   def __init__(self):
      self.verified_transactions = []
      self.previous_block_hash = ""
      self.Nonce = ""


