from socket import AF_INET, socket, SOCK_STREAM

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 8888))

msg = 'Привет, сервер!'
s.send(msg.encode('utf-8'))
data = s.recv(4096)
print(data.decode('utf-8'))
s.close()

# print(tame_data.decode('utf-8'))