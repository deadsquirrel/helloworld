#!/usr/bin/env python
# -*- coding: utf-8 -*-


import socket

sock = socket.socket()

# host (all), port
sock.bind(('', 9090))

# мах кол-во подключений в очереди
sock.listen(1)
print 'listening... . . .  .   .    .     .'

#conn, addr = sock.accept()
#print 'conected:', addr

# получаем данные кусками по 1024б
# и возвращаем их клиенту в вехнем регистре

try:
    while True:
        conn, addr = sock.accept()
        print 'conected:', addr
        data = conn.recv(1024)
#    if not data:
#        break
        if data == 'quit':
#        conn.close()
            conn.send("kill!")
        conn.send(data.upper())
finally:
    conn.close()
