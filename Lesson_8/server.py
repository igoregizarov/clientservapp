import select
from socket import socket, SOCK_STREAM, AF_INET


def read_req(r_list, clients):
    responses = {}

    for sock in r_list:
        try:
            data = sock.recv(1024).decode('utf-8')
            responses[sock] = data
        except:
            print(f"Клиент {sock} отключился")
            clients.remove(sock)

    return responses


def write_resp(requests, w_list, clients):
    for sock in w_list:

        for _, request in requests.items():


        # if sock in requests:
            try:
                resp = request.encode('utf-8')
                sock.send(resp)
            except:
                sock.close()
                clients.remove(sock)


def main():
    address = ('', 8888)
    clients = []

    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(5)
    sock.settimeout(5)

    while True:
        try:
            conn, addr = sock.accept()
        except OSError as e:
            pass
        else:
            print(f"Получен запрос на соединение от {addr}")
            clients.append(conn)
        finally:
            r_list = []
            w_list = []

            try:
                r_list, w_list, e_list = select.select(clients, clients, [], 10)
            except:
                pass

            requests = read_req(r_list, clients)
            if requests:
                write_resp(requests, w_list, clients)


print('Working....')
main()