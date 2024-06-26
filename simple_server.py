import socket
from common_functions import verify_digital_signature

HOST = '127.0.0.1'
PORT = 9876

def server_mode():
    with open("public.pem", "rb") as pub_file:
        rsa_pub = pub_file.read()

    print("Server RSA Public Key:", rsa_pub.decode())
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(4096)
                if not data:
                    break
                message, signature = data.split(b'||')
                print(f"Received message: {message.decode()}")
                if verify_digital_signature(message.decode(), signature, rsa_pub):
                    print("Message received and verified.")
                else:
                    print("Message verification failed.")
                conn.sendall(b"ACK")

if __name__ == '__main__':
    server_mode()
