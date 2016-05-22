#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
демонстрирует как использовать режим edge-triggered. В строках 25, 36 и 45 
вводятся циклы, которые работаю пока не возникнет исключение (или станет
известно, что все данные обработаны). Строки 32, 38 и 48 ловят исключения
Наконец, строки 16, 28, 41 и 51 добавляют маску EPOLLET, которая задает 
режим edge-triggered.
'''

import socket, select
     
EOL1 = b'\n\n'
EOL2 = b'\n\r\n'
response = b'HTTP/1.0 200 OK\r\nDate: Mon, 1 Jan 1996 01:01:01 GMT\r\n'
response += b'Content-Type: text/plain\r\nContent-Length: 13\r\n\r\n'
response += b'Hello, world!'

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind(('0.0.0.0', 8080))
serversocket.listen(1)
serversocket.setblocking( 0)

epoll = select.epoll()
epoll.register(serversocket.fileno(), select.EPOLLIN | select.EPOLLET)
     
try:
    connections = {}; requests = {}; responses = {}
    while True:
        events = epoll.poll(1)
        for fileno, event in events:
            if fileno == serversocket.fileno():
                try:
                    while True: #25
                        connection, address = serversocket.accept()
                        connection.setblocking( 0)
                        epoll.register(connection.fileno(), select.EPOLLIN | select.EPOLLET) #28
                        connections[connection.fileno()] = connection
                        requests[connection.fileno()] = b''
                        responses[connection.fileno()] = response
                except socket.error: #32
                    pass
            elif event & select.EPOLLIN:
                try:
                    while True: #36
                        requests[fileno] += connections[fileno].recv(1024)
                except socket.error: #38
                    pass
                if EOL1 in requests[fileno] or EOL2 in requests[fileno]:
                    epoll.modify(fileno, select.EPOLLOUT | select.EPOLLET) #41
                    print('-'*40 + '\n' + requests[fileno].decode()[:-2])
            elif event & select.EPOLLOUT:
                try:
                    while len(responses[fileno]) >  0: #45
                        byteswritten = connections[fileno].send(responses[fileno])
                        responses[fileno] = responses[fileno][byteswritten:]
                except socket.error: #48
                    pass
                if len(responses[fileno]) ==  0:
                    epoll.modify(fileno, select.EPOLLET) #51
                    connections[fileno].shutdown(socket.SHUT_RDWR)
            elif event & select.EPOLLHUP:
                epoll.unregister(fileno)
                connections[fileno].close()
                del connections[fileno]
finally:
    epoll.unregister(serversocket.fileno())
    epoll.close()
    serversocket.close()
