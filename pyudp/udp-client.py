#!/usr/bin/env python

import socket

skt = socket.socket(type = socket.SOCK_DGRAM)
skt.bind(("0.0.0.0", 5006))

skt.sendto(bytes("localhost", "utf-8"), ("127.0.0.1", 5005))

while True:
    data, addr = skt.recvfrom(1024)
    rec = 0
    for i in range(0,4):
        rec += data[i] << (i * 8)

    print("recieved", rec)
