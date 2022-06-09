import socket
import pickle
from messages.simple_message import SimpleMessage

if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 9999))
    server_socket.listen()
    clients = []
    print(f'Server started')
    server_message = SimpleMessage()

    while True:
        (client_socket, address) = server_socket.accept()
        if client_socket:
            clients.append((client_socket, address))
            print(f'client added {address}')
        buffer = pickle.dumps(server_message.increment())
        for client_sock, client_address in clients:
            total_sent = 0
            while total_sent < len(buffer):
                sent = client_sock.send(buffer)
                if sent == 0:
                    raise RuntimeError(f'The socket is broken')
                total_sent = total_sent + sent


