import socket
import pickle
import select
from messages.simple_message import SimpleMessage
import time

if __name__ == '__main__':
    print(f'Hello from socket')
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    retry_connection = True
    while retry_connection:
        try:
            client_socket.connect(('127.0.0.1', 9999))
            retry_connection = False
        except ConnectionRefusedError:
            print(f'The server is not available yet. Retry in 10 sec')
            time.sleep(10)
    chunks = []
    bytes_res = 0
    # inputs = [client_socket]
    while client_socket:
        # ready_to_read, ready_to_write, in_error = select.select(inputs,
        #                                                         None,
        #                                                         inputs)
        # if client_socket in ready_to_read:
        #     chunks = []
        #     bytes_res = 0
        #     while bytes_res < 4:
        #         chunk = client_socket.recv(4)
        #         if len(chunk) != 0:
        #             chunks.append(chunk)
        #             bytes_res = bytes_res + len(chunk)
        msg_bytes: bytes = None
        msg_bytes: bytes = client_socket.recv(4096)
        if msg_bytes != b'':
            # msg: SimpleMessage = pickle.loads(b''.join(chunks))
            msg: SimpleMessage = pickle.loads(msg_bytes)
            print(f'The message {msg} successfully received by the client')
