import socket
import threading
from decrypt import Decrypt

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

HEADER = 64

Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Server.bind(ADDR)


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] : {addr} connected")

    connected = True

    while connected:
        msg_recv = conn.recv(HEADER).decode('utf-8')
        if not msg_recv:
         break

        msg_length = int(msg_recv)

        msg = conn.recv(msg_length)
        decrypt_msg = Decrypt(msg)
        print(f"{addr} : {decrypt_msg}")

        if decrypt_msg == "disconnect":
            print("[CONNECTION CLOSED] : {addr}")
            connected = False

    conn.close()


def start():
    Server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")

    while True:
        conn, addr = Server.accept()

        thread = threading.Thread(
            target=handle_client,
            args=(conn, addr)
        )

        thread.start()

        print(f"[ACTIVE CONNECTIONS] : {threading.active_count() - 1}")


print("[STARTING] Server is starting...")
start()