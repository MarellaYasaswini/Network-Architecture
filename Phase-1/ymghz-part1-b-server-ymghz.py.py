import socket
import os
host=socket.gethostbyname("10.151.7.90")
port=2400
s=socket.socket()
s.bind((host,port))
s.listen(1)
c,addr=s.accept()
while True:
    data = c.recv(256000000).decode('utf-8')
    if data == 'exit':
        d = 'Server Gone'
        c.send(d.encode("utf-8"))
        break
    else:
        k = open('client.txt','w')
        k.write(data)
        k.close()
        print(str(data))
        v=data +'\nAdded by the server'
        c.send(v.encode("utf-8"))
c.close()

