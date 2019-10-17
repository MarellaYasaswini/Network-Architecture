import socket
host='10.151.2.20'
port=2400
s=socket.socket()
s.connect((host,port))
m=input("Press enter to send file -->")
g=open('client.txt','rb')
n=g.read()
while True:
    if m=='exit':
       s.send(m.encode("utf-8"))
       data=s.recv(256000000).decode("utf-8")
       print(str(data))
       s.close()
    else:
       s.send(n)
       break
a = "done sending"
s.send(a.encode("utf-8"))
data = s.recv(256000000).decode("utf-8")
print(str(data))
m=input()
