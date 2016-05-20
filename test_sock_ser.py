#!/usr/bin/env python
# -*- coding: utf-8 -*-


import socket


EOL1 = b'\n\n'
EOL2 = b'\n\r\n'
response = b'HTTP/1.0 200 OK\r\nDate: Mon, 1 Jan 1996 01:01:01 GMT\r\n'
response += b'Content-Type: text/plain\r\nContent-Length: 13\r\n\r\n'
response += b'Hello, world!'
 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#sock = socket.socket()
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
