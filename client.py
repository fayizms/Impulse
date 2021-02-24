import socket
import sys

IP = socket.gethostbyname(socket.gethostname())
PORT = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, PORT))

DC_CODE = "#DC#"

def send_message(message):
    msg = message.encode('utf-8')
    msg_data = len(msg)
    send_data = str(msg_data).encode('utf-8')
    send_data += b'' * (64 - len(send_data))
    client.send(send_data)
    client.send(message.encode('utf-8'))

while True:
    try:
        msg_input = input("Input Message")
        send_message(msg_input)
    except KeyboardInterrupt:
        print("\nDisconnecting From Server")
        send_message(DC_CODE)
        sys.exit()
