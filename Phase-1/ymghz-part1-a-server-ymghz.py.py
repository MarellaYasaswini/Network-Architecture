import socket
host=socket.gethostbyname("10.205.7.26")
port=2400
t=socket.socket()
t.bind((host,port))
t.listen(1)
g,addr=t.accept()
while True:
    data = g.recv(1024).decode('utf-8')
    print(data)
    if data == 'Bye from Client Lalith Chandra Attaluri':
        b='Bye from Server- Yasaswini Marella'
        g.send(b.encode("utf8"))
        break
    elif data == 'Hello from Client Lalith Chandra Attaluri':
        a = 'Hello from Server- Yasaswini Marella'
        g.send(a.encode("utf8"))
    else:
        print(data)
        g.send(data.encode("utf8"))
g.close()