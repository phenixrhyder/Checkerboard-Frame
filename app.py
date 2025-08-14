import gradio as gr
import os

# --- This is the new, more robust version ---

# Define the HTML to be injected. This includes the Tailwind CSS script and the Google Font link.
# This ensures they are loaded correctly even inside an iframe.
html_injector = """
<script src="https://cdn.tailwindcss.com"></script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
"""

# Get the absolute path to the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
# Join that directory path with the filename to get the full path to index.html
html_file_path = os.path.join(script_dir, 'index.html')

# Read the entire content of the index.html file using the full path
try:
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
except FileNotFoundError:
    html_content = "<h1>Error: index.html not found.</h1><p>Please make sure 'index.html' is in the root of your repository.</p>"

# Create and launch the Gradio interface
# We pass the HTML injector to the <head> of the document Gradio creates.
with gr.Blocks(title="Frame Studio", head=html_injector) as demo:
    # Use gr.HTML() to render your full HTML file.
    gr.HTML(html_content)

# Launch the app
if __name__ == "__main__":
    demo.launch()
