import sys
import socket
import threading
from datetime import datetime
import pytz

version = 1.0

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
    date_time = GetTime()
    print(f"\n[{date_time}] <{addr[0]}> Connected to Server\n")

    isConnected = True
    while isConnected:
        try:
            msg = conn.recv(10)     # Receive Header
            if msg:
                d_msg = msg.decode('utf-8')
                client_message = conn.recv(int(d_msg))
                c_msg = client_message.decode('utf-8')

                if not c_msg == DC_CODE:
                    date_time = GetTime()
                    print(f"[{date_time}] <{addr[0]}> - {c_msg}")

                else:
                    print(f"\n[{date_time}] <{addr[0]}> Disconnected from server\n")
                    isConnected = False

        except ConnectionResetError:
            date_time = GetTime()

            print(f"\n[*] ({date_time}) <{addr[0]}> Forcibly Disconnected from server\n")
            isConnected = False




def GetTime():
    date = current.strftime('%Y-%m-%d')
    time = current.strftime('%H:%M:%S')
    date_time = f"{date} || {time}"
    
    return date_time

try:
    print(f"\nImpulse Terminal [Official Build v{version}] \n(c) 2021 Beta Technologies. All rights reserved.")
    print("\n[*] Activating Server..")
    print("[*] Server Succesfully Activated\n")
    start()

except KeyboardInterrupt:
    print("[*] Interrupt Requested")
    print("[*] Application Exiting")
    sys.exit()
