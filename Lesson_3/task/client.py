from socket import AF_INET, socket, SOCK_STREAM
import json
from sys import argv, exit
import time


def make_presence_msg():
    msg = {
        "action": "presence",
        "time": time.ctime()
    }
    return msg


if __name__ == '__main__':
    with open("common/settings.json") as f:
        data = json.load(f)

    name_script, host, = argv
    if host != '127.0.0.1':
        print('Error host')
        exit()

    s = socket(AF_INET, SOCK_STREAM)
    s.connect((host, data['port']))

    msg = make_presence_msg()
    msg = json.dumps(msg)

    s.send(msg.encode('utf-8'))
    data = s.recv(4096)
    data = data.decode('utf-8')
    data = json.loads(data)
    print(data["alert"])
    s.close()
