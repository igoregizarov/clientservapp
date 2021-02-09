from socket import AF_INET, socket, SOCK_STREAM
import time

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 8888))
s.listen(5)

while True:
    client, addr = s.accept()
    # print(client)
    # print(addr)
    data = client.recv(4096)
    print(data.decode('utf-8'))
    # timestr = time.ctime(time.time()) + '\n'
    # client.send(timestr.encode('utf-8'))
    msg = 'Привет, клиент!'
    client.send(msg.encode('utf-8'))
    client.close()