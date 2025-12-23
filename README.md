🗣️ Deepgram Live STT Streaming in Python

A beginner-friendly example showing how to use the Deepgram API to perform real-time speech-to-text (STT) transcription in Python using WebSockets (or SDK streaming). This project demonstrates how to connect to Deepgram, stream audio, and receive transcriptions live. 
Deepgram Docs

📌 Overview

This project contains a Python script (deepgram.py) that connects to the Deepgram Speech-to-Text API and transcribes audio in real time. As audio is streamed (e.g., microphone or other source), text is returned from Deepgram’s models. 
Deepgram Docs

🚀 Features

✔ Real-time voice transcription
✔ Works with live audio sources (mic, stream, etc.)
✔ Uses Deepgram’s Python SDK or WebSocket API
✔ Beginner-oriented — easy to follow

🧠 What You’ll Learn

This repo will help you understand:

How to install and configure the Deepgram Python SDK

How to stream audio in real time

How to receive and handle live text transcripts

🛠️ Prerequisites

Before you begin, make sure you have:

Python 3.7+ installed

A Deepgram API key (free accounts available) 
GitHub

pip (Python package installer)

📦 Installation

Clone the repository

git clone https://github.com/SaiyamCodes/Deepgram-liveSTT-streaming-python.git
cd Deepgram-liveSTT-streaming-python


Create a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows


Install requirements

pip install deepgram-sdk


If your code uses other dependencies (e.g., WebSocket libraries), add them here as well.

🔑 Getting Your Deepgram API Key

Go to Deepgram’s console: https://console.deepgram.com

Sign up (free credits available) 
GitHub

Create or copy your API key

Set it as an environment variable:

export DEEPGRAM_API_KEY="YOUR_DEEPGRAM_API_KEY"


(On Windows use set instead of export.)

🧪 Running the Example

From the project directory:

python deepgram.py


The script will read audio, send it to Deepgram for live transcription, and print the text as it arrives.

🧩 How It Works (Quick Explanation)

Initialize Deepgram client with your API key

Open a WebSocket connection to the Deepgram streaming endpoint

Send audio data (from a mic, file, or input source)

Receive transcription events in real time

Print or process the transcript text

This pattern is common for live streaming STT. 
Deepgram

🧠 Tips for Beginners

Make sure your mic is accessible and uses the correct sample rate

If you’re using WebSockets directly, ensure your network allows ws/wss connections

Start with short audio first to verify transcription before moving to live streams

❓ Troubleshooting

✔ Nothing is printed?
Make sure your API key is correctly set and you have audio input.

✔ Errors connecting?
Check your internet connection and firewall. Also verify keys and dependencies.

✔ Transcript output is empty?
Ensure the audio source is working and is sending actual sound.

❤️ Contributing

Feel free to:

Add better audio source support (microphone, file, browser)

Add example output to README

Create a GUI or web interface
