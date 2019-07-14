from socketserver import *
from threading import Thread
from socket import *
class httpsever():
    def __init__(self,addr):
        self.address = addr
        self.creat_socket()
        self.bind()
    def creat_socket(self):
        self.sockfd=socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    def bind(self):
        self.sockfd.bind(self.address)
        self.host = self.address[0]
        self.port = self.address[1]
    def sever_forever(self):
        self.sockfd.listen(3)
        while True:
            c,addr = self.sockfd.accept()

    pass
if __name__ == '__main__':
    ADDR = ('0.0.0.0',8000)
    httpd = httpsever(ADDR)
    httpd.server_forever()