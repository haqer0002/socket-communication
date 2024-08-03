import socket
import sys
import signal


def signal_handler(sig, frame):
    print('\tServer is shutting down....bye bye')
    sys.exit(0)


def start_server(host='127.0.0.1', port=65432):
    signal.signal(signal.SIGINT, signal_handler)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f'Server started, listening on {host}:{port}')
        while True:
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                conn.sendall(b'OK')
                print('Sent OK and closed connection')


if __name__ == '__main__':
    start_server()
