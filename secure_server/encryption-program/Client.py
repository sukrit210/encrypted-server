#! /usr/bin/env python3

import socket
from encrypt import Encrpyt

PORT = 5050
client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
#SERVER = input("enter server IP address:")
SERVER = '10.118.5.156'
ADDR = (SERVER,PORT)
client.connect(ADDR)
HEADER = 64
FORMAT = 'utf-8'
disconnector = 'disconnect'

def send(msg):
	msgen_lenght = len(msg)
	send_lenght = str(msgen_lenght).encode(FORMAT)
	send_lenght += b' ' * (HEADER - len(send_lenght))
	client.send(send_lenght)
	client.send(msg)
	if msg == b'glvfrqqhfw':
		pass
	else:
		send(Encrpyt())
    # msg = Encrpyt()
    # msg_len = len(msg)
    # sent_lenght = str(msg_len).encode(FORMAT)
    # send_lenght = b' ' * (HEADER - len(send_lenght))
    # client.send(send_lenght)
    # client.send(msg)
    
send(Encrpyt())


