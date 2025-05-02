# server.py

import socket
import time

HOST = 'localhost' # For same computer as client
PORT = 20000 # Low numbers are reserved for SSH, HTTP, SQL, et al.

sock = socket.socket()

try:
    sock.bind((HOST, PORT)) # Note tuple!

except Exception as e:

    print('bind() failed ' + str(e))
    exit(0)

sock.listen(1) # handle up to 1 back-logged connection

print('Waiting for a client ...')

client, address = sock.accept()

print('Accepted connection')

num=1

while True:

    try:
        msg=str(num)
        client.send(msg.encode())
        time.sleep(0.01)
        num+=1
   

    except Exception as e:
        print('Failed to transmit: ' + str(e))
        break
   


client.close()
sock.close
