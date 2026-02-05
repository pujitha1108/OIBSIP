🎙️ Hunterdii – Python Voice Assistant

Hunterdii is a simple Python-based voice assistant that can perform everyday tasks like searching Wikipedia, opening websites, playing music, sending emails, telling the time, and controlling basic system applications using voice commands.

 🚀 Features

- 🎤 Speech Recognition (Voice Commands)
- 🗣️ Text-to-Speech Responses
- 📚 Wikipedia Search
- 🌐 Google & YouTube Search
- 🎶 Play Music from YouTube Music
- ⏰ Tell Current Time
- 📧 Send Emails via Gmail
- 📝 Open Notepad
- 🧮 Open Calculator
- 💻 Open Command Prompt
- 🔄 Restart / Shutdown System
- 📂 Open Custom Files or Programs

 🛠️ Technologies Used

 **Python 3**
 **pyttsx3** – Text-to-Speech
 **SpeechRecognition** – Speech Input
 **PyAudio** – Microphone Input
 **Wikipedia API**
 **PyAutoGUI**
 **SMTP (Gmail)**

 📦 Required Python Libraries

Install all dependencies using:

```bash
pip install pyttsx3
pip install SpeechRecognition
pip install wikipedia
pip install pyautogui
pip install pyaudio
⚠️ Note:
If pyaudio installation fails on Windows, download the .whl file from:
https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
Then install using:

pip install PyAudio-<version>.whl

⚙️ Configuration

1️⃣ Email Setup
Edit the sendEmail() function:

server.login('your_email@gmail.com', 'your_app_password')
Enable 2-Step Verification in Gmail

Generate an App Password

Replace credentials in code

⚠️ Never share your real password publicly

2️⃣ Email Dictionary
Add known contacts:

email_dict = {
    "friend": "friend@example.com",
    "family": "family@example.com"
}
3️⃣ Change Assistant Name
Inside wishMe() function:

assistant_name = "Hunterdii"
🎤 Sample Voice Commands
Command	Action
"Wikipedia Elon Musk"	Searches Wikipedia
"Open YouTube"	Opens YouTube
"Open Google"	Opens Google
"Play music"	Plays YouTube Music
"What is the time"	Tells current time
"Search Google for Python"	Google search
"Search YouTube for AI"	YouTube search
"Send email to friend"	Sends email
"Open notepad"	Opens Notepad
"Open calculator"	Opens Calculator
"Shutdown"	Shuts down PC
"Restart"	Restarts PC

▶️ How to Run the Project

Clone the repository or download the files
Open terminal / command prompt
Run the Python file:

python main.py

Speak your commands 🎙️

📂 Project Structure
├── main.py
├── README.md
⚠️ Limitations
Requires active internet for speech recognition
Gmail SMTP requires app password
Designed primarily for Windows OS

🌟 Future Enhancements

GUI Interface
Wake Word Detection
AI-based Chat Responses
WhatsApp & Telegram Integration
Multilingual Voice Support

👩‍💻 Author
Amberi Pujitha
B.Tech – Artificial Intelligence & Machine Learning
📍 Hyderabad, India

📜 License
This project is open-source and free to use for educational purpose.