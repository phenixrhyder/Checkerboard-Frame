import gradio as gr
import os

# Get the absolute path to the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
# Join that directory path with the filename to get the full path to index.html
html_file_path = os.path.join(script_dir, 'index.html')

# Read the entire content of the index.html file using the full path
try:
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
except FileNotFoundError:
    html_content = "<h1>Error: index.html not found.</h1>"

# Create and launch the Gradio interface
with gr.Blocks(title="Frame Studio") as demo:
    gr.HTML(html_content)

demo.launch()

