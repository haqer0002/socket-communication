import socket


def connect_to_server(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        data = s.recv(1024)
    print('Received', repr(data))


if __name__ == "__main__":
    try:
        connect_to_server()
    except Exception as e:
        print(f"The error occurred: {e}")
        print("Please try connecting to the server again...")
