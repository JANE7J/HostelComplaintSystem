# ==============================
# Hostel Complaint Server
# Socket Programming - DS Lab
# ==============================

print("SERVER FILE STARTED")   # <-- MUST PRINT

import socket
import threading

HOST = "127.0.0.1"
PORT = 5000

# In-memory storage
complaints = []


def handle_client(conn, addr):
    print(f"[CONNECTED] {addr}")

    try:
        data = conn.recv(1024).decode()

        if data:
            print(f"[RECEIVED] {data}")

            room, category, description = data.split("|")

            complaint = {
                "room": room,
                "category": category,
                "description": description
            }

            complaints.append(complaint)

            print("[STORED] Complaint added")
            print("[ALL COMPLAINTS]", complaints)

            conn.sendall(b"Complaint received successfully")

    except Exception as e:
        print("[ERROR]", e)

    finally:
        conn.close()
        print(f"[DISCONNECTED] {addr}")


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"[SERVER RUNNING] Listening on {HOST}:{PORT}")

    while True:
        conn, addr = server_socket.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CLIENTS] {threading.active_count() - 1}")


# ENTRY POINT (DO NOT REMOVE)
start_server()
