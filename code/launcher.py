import webbrowser
import subprocess
import threading
import time
import os

# Function to run the Flask app (runs app.py)
def run_flask():
    subprocess.run(["python", "app.py"])

# Start the Flask app in a separate thread
flask_thread = threading.Thread(target=run_flask)
flask_thread.daemon = True
flask_thread.start()

# Wait briefly to ensure Flask starts
time.sleep(2)

# Open the main.html directly from filesystem
main_path = os.path.abspath("index.html")
webbrowser.open(f"file://{main_path}")
