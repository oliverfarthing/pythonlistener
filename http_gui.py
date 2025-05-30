import threading
import tkinter as tk
from flask import Flask
import queue

# Create Flask app
app = Flask(__name__)

# Queue to communicate between Flask thread and Tkinter main thread
q = queue.Queue()

@app.route('/hello')
def hello():
    q.put("Hello World")
    return "Message received, GUI updated."

def run_flask():
    app.run(port=5000)

def check_queue():
    try:
        msg = q.get_nowait()
    except queue.Empty:
        msg = None

    if msg:
        label.config(text=msg)
    root.after(100, check_queue)  # Check the queue every 100ms

# Setup Tkinter GUI
root = tk.Tk()
root.title("HTTP Request Listener")

label = tk.Label(root, text="Waiting for HTTP request...", font=("Arial", 18))
label.pack(pady=20, padx=20)

# Start Flask server in a background thread
flask_thread = threading.Thread(target=run_flask, daemon=True)
flask_thread.start()

# Start checking the queue for new messages
root.after(100, check_queue)

root.mainloop()
