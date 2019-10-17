import socket
host = socket.gethostbyname("10.205.3.192")
port = 2400
s = socket.socket()
s.connect((host,port))
m = input("enter -->")
while True:
    if m == 'Bye from Client Yasaswini Marella':
        s.send(m.encode('utf8'))
        data = s.recv(1024).decode('utf-8')
        print(data)
        break
        m = input()
    elif m == 'Hello from Client Yasaswini Marella':
        s.send(m.encode('utf8'))
        data = s.recv(1024).decode('utf-8')
        print(data)
        m = input()
    else:
        s.send(m).encode('utf8')
        data = s.recv(1024).decode('utf-8')
        print(data)
s.close()
