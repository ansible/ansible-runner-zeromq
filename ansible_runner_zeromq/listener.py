import zmq


def listen(socket_url):
    context = zmq.Context()
    receiver = context.socket(zmq.PULL)
    receiver.bind(socket_url)

    while True:
        msg = receiver.recv_json()
        print(msg)
