import socket
import pickle
from messages.simple_message import SimpleMessage

if __name__ == '__main__':
    print(f'Hello from socket')
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 9999))
    chunks = []
    bytes_res = 0
    while True:
        chunks = []
        bytes_res = 0
        while bytes_res < 4:
            chunk = client_socket.recv(4)
            if len(chunk) != 0:
                chunks.append(chunk)
                bytes_res = bytes_res + len(chunk)
        msg: SimpleMessage = pickle.loads(b''.join(chunks))

