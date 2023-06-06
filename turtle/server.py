from socket import socket,SOCK_STREAM,AF_INET
from base64 import b64encode
from json import dumps
from threading import Thread
# family=AF_INET - IPv4地址
    # family=AF_INET6 - IPv6地址
    # type=SOCK_STREAM - TCP套接字
    # type=SOCK_DGRAM - UDP套接字
    # type=SOCK_RAW - 原始套接字
def main():
    class FileTransferHandler(Thread):
        def __init__(self,cclient):
            super().__init__()
            self.cclient=cclient
        def run(self):
            my_dict={}
            my_dict['fliename']='guge.png'
            my_dict['filedata']=data
            json_str=dumps(my_dict)
            self.cclient.send(json_str.encode('utf-8'))

    server=socket()
    server.bind(('172.22.36.21',4567))
    server.listen(512)
    print("开始监听")
    with open('turtle\guge.png','rb') as f:
        data=b64encode(f.read()).decode('utf-8')  
    while True:
        client,addr=server.accept()
        FileTransferHandler(client).start()

if __name__=='__main__':
    main()
