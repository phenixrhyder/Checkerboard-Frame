import gradio as gr
import os

# --- THIS IS THE FIX ---
# Get the absolute path to the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
# Join that directory path with the filename to get the full path to index.html
html_file_path = os.path.join(script_dir, 'index.html')

# Read the entire content of the index.html file using the full path
try:
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
except FileNotFoundError:
    # If the file is not found, display an error message instead of crashing
    html_content = """
    <div style="font-family: sans-serif; text-align: center; padding: 2rem;">
        <h1 style="color: #ef4444;">Error: index.html not found</h1>
        <p style="color: #d1d5db;">Please make sure the 'index.html' file is in the same directory as 'app.py' in your repository.</p>
    </div>
    """

# Create a Gradio Blocks interface
with gr.Blocks(title="Frame Studio", css="body {background-color: #111827;}") as demo:
    # Use gr.HTML() to render your full HTML file.
    gr.HTML(html_content)

# Launch the app
if __name__ == "__main__":
    demo.launch()
