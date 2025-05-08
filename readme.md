# Real-Time Updates with Server-Sent Events (SSE) in Django

This project demonstrates how to use **Server-Sent Events (SSE)** to send real-time updates from a **Django** backend to a frontend using plain JavaScript. By replacing polling with SSE, we can reduce server load and provide more efficient real-time communication.

## 🛠️ Prerequisites

Before you begin, make sure you have the following installed:

- Python 3.10.10
- pip (Python package manager)
- Django (5.2.1 or later)
- Git (for cloning the repository)

## ⚡ Installation

### 1. Clone the repository

```bash
git clone https://github.com/ShivaBsnt/ServerSentEvents.git
cd ServerSentEvents
```

### 2. Set up a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
### 3. Install the dependencies
```bash
pip install -r requirements.txt
```
### 4. Run the Django development server
```bash
 python manage.py runserver 
 ```
Once the server is running, open your browser and visit http://127.0.0.1:8000/

## 🚀 How it Works
The Django backend streams real-time data to the frontend using the /events/ endpoint.

The frontend uses JavaScript's EventSource to listen for updates from the server.

Server-Sent Events (SSE) enables efficient real-time communication by keeping a single connection open.

## 💡 Features
- Real-time updates using SSE without needing frequent polling.

- Simple and lightweight implementation using Django and JavaScript.

- Automatic reconnection in case of a connection failure.

## 📄 License
This project is open-source and available under the MIT License.