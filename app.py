# app.py
from flask import Flask, send_from_directory

# This creates the web server.
app = Flask(__name__)

# This tells the server to look for your main HTML file.
@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

# This runs the server.
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
