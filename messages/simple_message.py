class SimpleMessage:
    greeting: str = 'Server message'
    msg_id: int

    def __init__(self, msg_id=0):
        self.msg_id = msg_id

    def increment(self):
        self.msg_id += 1



