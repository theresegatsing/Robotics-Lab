# client.py
from threading import Thread
import socket
import time


def updater(vals):
   

    HOST = 'localhost'
    PORT = 20000

    sock = socket.socket()

    try:
        sock.connect((HOST, PORT)) # Note tuple!

    except Exception as e:
        print('connect() failed: ' +str(e))

    while True:

        try:
            msg = sock.recv(80)
           
            message=msg.decode()
            vals[0] = int(message)
        except:
            print('Failed to receive')
            break
    sock.close()


vals=[0]
thread1=Thread(target=updater, args=(vals,))
thread1.daemon=True
thread1.start()


while True:
    time.sleep(1)
    print(vals)
