# ==============================
# Hostel Complaint Client
# Socket Programming - DS Lab
# ==============================

import socket

HOST = "127.0.0.1"
PORT = 5000

def send_complaint():
    room = input("Enter Room Number: ")
    category = input("Enter Category (Water/Electricity/Cleanliness/Other): ")
    description = input("Enter Complaint Description: ")

    message = f"{room}|{category}|{description}"

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))

        client_socket.sendall(message.encode())

        response = client_socket.recv(1024).decode()
        print("\nServer Response:", response)

        client_socket.close()

    except Exception as e:
        print("Error:", e)


send_complaint()
