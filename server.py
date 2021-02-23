import sys
import socket
import threading
from datetime import datetime
import pytz

version = 2.0

IP = socket.gethostbyname(socket.gethostname())
PORT = 8080
timezone = pytz.timezone('Asia/Calcutta')
current = datetime.now(timezone)

DC_CODE = "#DC#"

def start():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((IP, PORT))
        server.listen()

        print("[*] Initializing Sockets.. Successfull")
        print("[*] Sockets Binded Succesfully")
        print(f"[*] Server Running on [PORT : {PORT}]")

    except Exception as SocketError:
        print("[*] Error Initializing Socket")
        sys.exit()

    while True:
        connection, address = server.accept()
        ClientThread = threading.Thread(target=ConnectClient, args=(connection, address))
        ClientThread.start()

def ConnectClient(conn, addr):
    date = current.strftime('%Y-%m-%d')
    time = current.strftime('%H:%M:%S')
    print(f"\n[{date} || {time}] {addr} Connected to Server\n")

    isConnected = True
    while isConnected:
        msg = conn.recv(10)     # Receive Header
        if msg:
            date = current.strftime('%Y-%m-%d')
            time = current.strftime('%H:%M:%S')

            d_msg = msg.decode('utf-8')
            client_message = conn.recv(int(d_msg))
            c_msg = client_message.decode('utf-8')

            if not c_msg == DC_CODE:
                print(f"[{date}  {time}] [{addr}] - {c_msg}")

            else:
                print(f"[({addr}) - Disconnected From Server] ")
                isConnected = False

try:
    print(f"\nImpulse Terminal [Development Build v{version}] \n(c) 2021 Beta Technologies. All rights reserved.")
    print("\n[*] Activating Server..")
    print("[*] Server Succesfully Activated\n")
    start()
except KeyboardInterrupt:
    print("[*] Interrupt Requested")
    print("[*] Application Exiting")
    sys.exit()
