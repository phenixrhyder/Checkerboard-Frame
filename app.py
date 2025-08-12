from flask import Flask, send_from_directory

# Create a Flask web server
app = Flask(__name__, static_folder='.', static_url_path='')

# Define the route for the root URL ('/')
@app.route('/')
def index():
    # Send the index.html file from the current directory
    return send_from_directory('.', 'index.html')

# This allows the app to be run by a production server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7860)
