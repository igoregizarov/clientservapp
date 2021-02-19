from socket import AF_INET, socket, SOCK_STREAM
import time
import json


def send_msg_to_client(var):
    if var == 'presence':
        msg = {
            "response": 200,
            "alert": "Connect is done!",
            "time": time.ctime()
        }
    else:
        msg = {
            "response": 400,
            "alert": "Something wrong!",
            "time": time.ctime()
        }
    return msg


if __name__ == '__main__':
    from common.configs import *

    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('', PORT))
    s.listen(LISTEN)

    while True:
        client, addr = s.accept()
        data = client.recv(4096)
        data = data.decode('utf-8')
        data = json.loads(data)
        msg = send_msg_to_client(data['action'])
        msg = json.dumps(msg)
        client.send(msg.encode('utf-8'))
        client.close()
