from socket import *
from threading import Thread
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)
s = socket()
s.bind(ADDR)
s.listen(5)

def handle(connfd):
    while True:
        data = connfd.recv(1024).decode()
        if not data:
            break
        print(data)
        connfd.send(b'ok')
while True:
    try:
        connfd,addr = s.accept()
    except KeyboardInterrupt:
        s.close()
        print('服务器退出')
        break
    except Exception as e:
        print('错误',e)
        continue
t = Thread(target=handle,args=(connfd,))
t.setDaemon(True)
t.start()