#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

sock = socket.socket()
chost = raw_input('Enter hostname for connections: ')
sock.connect((chost, 9090))
#sock.connect(('52.38.123.102', 9090))

msg = raw_input('Enter you message: ')
sock.send(msg)

data = sock.recv(1024)
sock.close()

print data
