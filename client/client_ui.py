# ==============================
# Hostel Complaint Client UI
# Socket Programming - DS Lab
# ==============================

import socket
import tkinter as tk
from tkinter import messagebox

HOST = "127.0.0.1"
PORT = 5000

def submit_complaint():
    room = entry_room.get()
    category = category_var.get()
    description = text_desc.get("1.0", tk.END).strip()

    if room == "" or description == "":
        messagebox.showerror("Error", "All fields are required")
        return

    message = f"{room}|{category}|{description}"

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))

        client_socket.sendall(message.encode())

        response = client_socket.recv(1024).decode()
        client_socket.close()

        messagebox.showinfo("Success", response)

        # Clear fields after submission
        entry_room.delete(0, tk.END)
        text_desc.delete("1.0", tk.END)

    except Exception as e:
        messagebox.showerror("Connection Error", str(e))


# -------- UI DESIGN --------
root = tk.Tk()
root.title("Hostel Complaint Management System")
root.geometry("400x300")

tk.Label(root, text="Room Number").pack(pady=5)
entry_room = tk.Entry(root, width=30)
entry_room.pack()

tk.Label(root, text="Category").pack(pady=5)
category_var = tk.StringVar(value="Water")
tk.OptionMenu(
    root,
    category_var,
    "Water",
    "Electricity",
    "Cleanliness",
    "Other"
).pack()

tk.Label(root, text="Description").pack(pady=5)
text_desc = tk.Text(root, width=35, height=5)
text_desc.pack()

tk.Button(
    root,
    text="Submit Complaint",
    command=submit_complaint,
    bg="blue",
    fg="white"
).pack(pady=15)

root.mainloop()
