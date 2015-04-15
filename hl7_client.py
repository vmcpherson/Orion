#!/usr/bin/env python


# Exampel HL7 client application
#


import socket

SB = 0x0b
EB = 0x1c
CR = 0x0d


TCP_IP = '127.0.0.1'
TCP_PORT = 8888
BUFFER_SIZE = 1024



SB = 0x0b
EB = 0x1c
CR = 0x0d

message_text = b'Hello, World!'
message_bytes = bytearray(1 + len(message_text) + 2)
message_bytes[0] = SB
mv = memoryview(message_bytes)
mv[1:1 + len(message_text)] = message_text
message_bytes[1 + len(message_text)] = EB
message_bytes[1 + len(message_text) + 1] = CR

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
print "Connected"
s.send(message_bytes)
print "Sent"
data = s.recv(BUFFER_SIZE)
print "Received"
s.close()
  
print "received data:", data
