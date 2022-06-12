import pickle


class SimpleMessage:
    _greeting: str = 'Server message'
    _msg_id: int

    def __init__(self, greeting='Server message', msg_id=0):
        self._greeting = greeting
        self._msg_id = msg_id

    def increment(self):
        self._msg_id += 1

    def __str__(self):
        return f'MSG: {self._greeting} {self._msg_id}'


if __name__ == '__main__':
    msg = SimpleMessage()
    print(msg)
    bytes_msg = pickle.dumps(msg)
    loaded_msg: SimpleMessage = pickle.loads(bytes_msg)
    print(loaded_msg)
