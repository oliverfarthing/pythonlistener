Requirements

* Python installed on your computer
* The Flask Python package installed
* Tkinter (usually included with Python by default) validate (python -m tkinter)

Common Tips

* Make sure no other program is using port 5000 on your machine.
* Run the terminal or command prompt as administrator if you have permission issues.
* If you want to stop the program, just close the GUI window or press `Ctrl+C` in the terminal.****

---
Step 1: Verify Python Installation

1. Open your command prompt (Windows) or terminal (macOS/Linux).

2. Check Python version by running:

python --version

4. If Python is not installed, download and install it from [python.org](https://www.python.org/downloads/).

---
Step 2: Install Flask, Flask is a lightweight web framework needed to handle HTTP requests.

1. Run this command in your command prompt or terminal:

pip install flask

---

Step 3: Save the Python Script

1. Copy the Python code into a text file and save it with a `.py` extension, for example:

http_gui.py

---
Step 4: Run the Python Script

1. Navigate to the folder where you saved the script. For example:

cd C:\temp

2. Run the script with:

python http_gui.py

3. A GUI window will open, displaying:

Waiting for HTTP request...

---
Step 5: Send the HTTP Request

1. Open a web browser or use a tool like `curl` or Postman, then access the URL:

Example using web browser in terminal:

http://127.0.0.1:5000/hello

Example using curl in terminal:

curl http://127.0.0.1:5000/hello

When the request is received, the GUI text will change to:

Hello World



