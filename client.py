import socket
import sys

HOST = socket.gethostbyname(socket.gethostname())
PORT = 8080
IP = socket.gethostbyname(socket.gethostname())
DC_CODE = "#DC#"

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((IP, PORT))

    print("[*] Initializing Sockets")
    print("[*] Connecting to Server..")
    print(f"[*] Successfully Connected to Server\t[Server IP : {HOST}]\n")

except Exception as exc:
    print("[*] Unable to connect to server")
    sys.exit()

def send(message):
    msg = message.encode('utf-8')
    msg_data = len(msg)
    send_data = str(msg_data).encode('utf-8')
    send_data += b'' * (64 - len(send_data))
    if not message == DC_CODE:
        try:
            client.send(send_data)
            client.send(message.encode('utf-8'))

        except ConnectionResetError:
            print("[*] Server Unavailable")
            sys.exit()
    else:
        try:
            client.send(send_data)
            client.send(message.encode('utf-8'))
        except ConnectionResetError:
            pass

while True:
    try:
        msg_input = input(f"{IP}> ")
        send(msg_input)
    except KeyboardInterrupt:
        send(DC_CODE)
        print("\n\n[*] Disconnecting From Server")
        sys.exit()
