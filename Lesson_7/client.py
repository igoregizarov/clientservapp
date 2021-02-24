from socket import socket, SOCK_STREAM, AF_INET
from sys import argv, exit

name, action = argv

address = ('localhost', 8888)
responses = []


def client(responses):
    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.connect(address)
        while True:
            if argv[1] == 'send':
                msg = input('Send massage:  ')
                if msg == 'exit':
                    break
                sock.send(msg.encode('utf-8'))
            elif argv[1] == 'read':
                data = sock.recv(1024).decode('utf-8')
                if data:
                    responses.append(data)
                    print('Massage from chat: ', data)
            else:
                print('ARGV "send" or "read"')
                exit()


if __name__ == '__main__':
    client(responses)
