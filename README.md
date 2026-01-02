# 🏢 Hostel Complaint Management System  
### Distributed Systems Lab Project

---

##  Problem Description

In hostel environments, students often face issues such as water supply problems, electricity failures, cleanliness concerns, or general maintenance issues. Traditionally, these complaints are handled manually, which can be inefficient, slow, and difficult to track.

The **Hostel Complaint Management System** is a distributed client–server application that allows students to submit complaints through a web interface. The system demonstrates core **Distributed Systems concepts** such as client–server architecture, protocol translation, socket communication, concurrency, and in-memory data storage.

This project focuses on **functional correctness and distributed communication**, not UI polish or persistent databases.

---

##  System Architecture Overview

The system follows a **three-layer distributed architecture**:

1. **Client Layer (Web UI)**
2. **Middleware Layer (HTTP Bridge Server)**
3. **Backend Layer (Socket-Based Complaint Server with In-Memory Storage)**

Each layer runs independently and communicates using well-defined protocols.

---

##  Communication Model Used

### 1️. Client → Middleware  
- **Protocol:** HTTP  
- **Method:** POST  
- **Data Format:** JSON  
- **Technology:** HTML, Tailwind CSS, JavaScript  

The student submits a complaint through a web form.  
JavaScript sends the complaint data as a JSON payload to the HTTP bridge server.

---

### 2️. Middleware → Backend  
- **Protocol:** TCP Socket  
- **Technology:** Python Socket Programming  

The HTTP Bridge Server translates the HTTP request into a TCP socket message and forwards the complaint data to the backend socket server.

---

### 3️. Backend → Middleware → Client  

The backend server processes the request and stores the complaint in memory.  
An acknowledgment is sent back through the same path.  
The client receives a success response and is redirected to a confirmation page.

---

## In-Memory Storage Design

Complaints are stored in a **Python list (array)** inside the socket-based backend server.

Each complaint is stored as a dictionary containing:
- Room Number  
- Complaint Category  
- Complaint Description  

No database is used, as per lab requirements.  
All data exists only during runtime and is lost when the server stops.

---

### Why In-Memory Storage?

In real distributed systems, not all data needs to be stored permanently.  
In-memory storage is commonly used for:
- Temporary records  
- Caching  
- Session data  
- Live service tracking  

This approach keeps the system lightweight and aligns with the lab focus on **distributed communication rather than storage complexity**.

---

##  Technologies Used

### Frontend (Client)
- HTML  
- Tailwind CSS  
- JavaScript  

### Middleware
- Flask (Python)  
- HTTP Server  
- Port: **8000**

### Backend
- Python Socket Programming  
- Multithreading  
- TCP Server  
- Port: **5000**

---

##  Steps to Run the Application

### 1️.  Clone the Repository
```bash
git clone https://github.com/JANE7J/HostelComplaintSystem.git
cd HostelComplaintSystem
