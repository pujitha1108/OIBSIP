🗨️ PYTHON CHAT ROOM WITH TKINTER GUI

A simple **chat room application** built with **Python sockets** and a **Tkinter GUI**.  
This project demonstrates how to combine networking (socket programming) with a graphical interface for real-time communication.

🚀 Features

- **Real-time messaging** using TCP sockets
- **User authentication** with username prompt
- **Modern chat bubbles** styled like WhatsApp
- **System notifications** (user join/leave events)
- **Scrollable chat area** with auto-scroll
- **Separate threads** for sending and receiving messages
- **Simple and clean Tkinter GUI**

📂 Project Structure
chat_client.py   # Client-side GUI code (Tkinter + sockets)
chat_server.py   # Server-side socket handler (to be created separately)
README.md                # Documentation

🛠️ Requirements
- Python 3.x
- Tkinter (comes pre-installed with Python)
- Basic knowledge of socket programming

📖 How It Works

~Server listens for incoming connections.
~Clients connect to the server and send their username.
~Messages are sent to the server, which broadcasts them to all connected clients.
~Tkinter GUI displays messages in styled bubbles with auto-scroll.

🔮 Future Improvements

~Emoji support 😃
~Private chat rooms
~File sharing
~User authentication with passwords
~Message encryption