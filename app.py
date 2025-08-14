import gradio as gr
import os

# --- THIS IS THE DEBUGGING VERSION ---

# Get the absolute path to the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
# Get the current working directory
cwd = os.getcwd()

# Construct the full path to index.html
html_file_path = os.path.join(script_dir, 'index.html')

# Try to read the index.html file
try:
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
except FileNotFoundError:
    # If the file is not found, create a detailed error message for debugging
    
    # List files in the script's directory
    try:
        script_dir_files = os.listdir(script_dir)
        script_dir_files_str = "<br>".join(script_dir_files)
    except Exception as e:
        script_dir_files_str = f"Could not list files: {e}"

    # List files in the current working directory
    try:
        cwd_files = os.listdir(cwd)
        cwd_files_str = "<br>".join(cwd_files)
    except Exception as e:
        cwd_files_str = f"Could not list files: {e}"

    # The HTML content will now be our debug output
    html_content = f"""
    <div style="font-family: monospace; color: #d1d5db; background-color: #1f2937; padding: 2rem; border-radius: 1rem; border: 1px solid #374151;">
        <h1 style="color: #ef4444; font-size: 1.5rem;">File Not Found Error</h1>
        <p style="color: #9ca3af; margin-top: 1rem;">The server could not find 'index.html'.</p>
        
        <h2 style="color: #f9fafb; margin-top: 2rem; border-bottom: 1px solid #374151; padding-bottom: 0.5rem;">Debugging Info:</h2>
        
        <h3 style="color: #60a5fa; margin-top: 1.5rem;">Expected File Path:</h3>
        <p>{html_file_path}</p>
        
        <h3 style="color: #60a5fa; margin-top: 1.5rem;">Files found in the script's directory ({script_dir}):</h3>
        <div style="background-color: #111827; padding: 1rem; border-radius: 0.5rem; margin-top: 0.5rem;">
            {script_dir_files_str}
        </div>

        <h3 style="color: #60a5fa; margin-top: 1.5rem;">Files found in the current working directory ({cwd}):</h3>
        <div style="background-color: #111827; padding: 1rem; border-radius: 0.5rem; margin-top: 0.5rem;">
            {cwd_files_str}
        </div>
    </div>
    """

# Create a Gradio Blocks interface
with gr.Blocks(title="Frame Studio Debug", css="body {{background-color: #111827;}}") as demo:
    # Use gr.HTML() to render your full HTML file or the debug info.
    gr.HTML(html_content)

# Launch the app
if __name__ == "__main__":
    demo.launch()
