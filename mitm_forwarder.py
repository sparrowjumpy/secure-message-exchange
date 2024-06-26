import socket

HOST = '127.0.0.1'
MITM_PORT = 9875
SERVER_PORT = 9876

def mitm_forwarder():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect((HOST, SERVER_PORT))

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, MITM_PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('MITM Forwarder connected by', addr)
            while True:
                data = conn.recv(4096)
                if not data:
                    break
                print("Forwarding data...")
                server_socket.sendall(data)
                response = server_socket.recv(4096)
                conn.sendall(response)

if __name__ == '__main__':
    mitm_forwarder()
