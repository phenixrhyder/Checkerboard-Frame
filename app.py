import gradio as gr

# Read the entire content of the index.html file
with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Create a Gradio Blocks interface
with gr.Blocks(title="Frame Studio") as demo:
    # Use gr.HTML() to render your full HTML file.
    # The content will be displayed inside a full-width, full-height iframe.
    gr.HTML(html_content)

# Launch the app
if __name__ == "__main__":
    demo.launch()
