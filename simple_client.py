import socket
from common_functions import generate_digital_signature

HOST = '127.0.0.1'
PORT = 9875

def client_mode():
    with open("private.pem", "rb") as priv_file:
        rsa_priv = priv_file.read()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            message = input("Enter message to send: ")
            if message.lower() == 'exit':
                break
            signature = generate_digital_signature(message, rsa_priv)
            s.sendall(message.encode() + b"||" + signature)
            response = s.recv(1024)
            print("Server response:", response.decode())

if __name__ == '__main__':
    client_mode()
