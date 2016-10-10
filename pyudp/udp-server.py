#!/usr/bin/env python

import socket
import random
import time

skt = socket.socket(type = socket.SOCK_DGRAM)

skt.bind(("0.0.0.0", 5005))

data, addr = skt.recvfrom(1024)

returnaddr = (data.decode(), addr[1])

print("sending data to", addr)

while True:
    skt.sendto(random.randint(0, 1024).to_bytes(4, "little"), returnaddr)
    time.sleep(1)
