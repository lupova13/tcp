import socket
import pickle
import select
import time
from messages.simple_message import SimpleMessage

if __name__ == '__main__':
    server_socket = None
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setblocking(False)
        server_socket.bind(('127.0.0.1', 9999))
        server_socket.listen(5)
        inputs = [server_socket]
        outputs = []
        print(f'Server started')
        server_message = SimpleMessage()

        while inputs:
            ready_to_read, ready_to_write, in_error = select.select(inputs,
                                                                    outputs,
                                                                    inputs + outputs)
            for s in ready_to_read:
                if s is server_socket:
                    (client_socket, address) = server_socket.accept()
                    client_socket.setblocking(False)
                    outputs.append(client_socket)
                    print(f'client added {address}')
            for s in ready_to_write:
                server_message.increment()
                buffer = pickle.dumps(server_message)
                total_sent = 0
                sent = s.send(buffer)

                # while total_sent < len(buffer):
                #     sent = s.send(buffer)
                #     if sent == 0:
                #         raise RuntimeError(f'The socket is broken')
                #     total_sent = total_sent + sent
                print(f'The message {server_message} successfully sent by the server')
                time.sleep(10)

            for s in in_error:
                outputs.remove(s)
                inputs.remove(s)
    finally:
        if server_socket:
            server_socket.close()


