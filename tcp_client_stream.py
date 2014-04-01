#!/usr/bin/python


import socket

TCP_IP = '192.168.2.126'
TCP_PORT = 5005
BUFFER_SIZE = 1024

um = 0

ip = raw_input("IP-Adresse: ") 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((ip, TCP_PORT))

try: 
    while True: 
        # nachricht = raw_input("Nachricht: ") 
        s.send(str(um)) 
        um = um + 1
        antwort = s.recv(1024) 
        print "[%d] [%s] %s" % (um,ip,antwort) 
finally: 
    s.close()