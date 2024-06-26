import socket

HOST = '127.0.0.1'
MITM_PORT = 9875
SERVER_PORT = 9876

def mitm_attacker():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect((HOST, SERVER_PORT))

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, MITM_PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('MITM Attacker connected by', addr)
            while True:
                data = conn.recv(4096)
                if not data:
                    break
                # Modify the data
                print("Intercepting and altering data...")
                if b'||' in data:
                    parts = data.split(b'||')
                    message = parts[0].replace(b"hello", b"goodbye")
                    data = message + b'||' + parts[1]
                server_socket.sendall(data)
                response = server_socket.recv(4096)
                conn.sendall(response)

if __name__ == '__main__':
    mitm_attacker()
