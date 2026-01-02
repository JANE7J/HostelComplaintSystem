from flask import Flask, request, jsonify
import socket
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5000


@app.route("/submit-complaint", methods=["POST"])
def submit_complaint():
    data = request.json

    room = data.get("room")
    category = data.get("category")
    description = data.get("description")

    message = f"{room}|{category}|{description}"

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((SERVER_HOST, SERVER_PORT))
        s.sendall(message.encode())
        response = s.recv(1024).decode()
        s.close()

        return jsonify({"status": "success", "message": response})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == "__main__":
    app.run(port=8000, debug=True)
