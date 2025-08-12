# app.py

import gradio as gr
from PIL import Image, ImageDraw
import tempfile

def create_checkerboard_frame(width, height, frame_thickness, square_size, color1, color2):
    """
    Generates a checkerboard frame with a transparent center.
    """
    # Create a new blank image in RGBA mode to support transparency
    image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)

    # Calculate how many squares fit on the canvas
    board_size_w = int(width / square_size) + 1
    board_size_h = int(height / square_size) + 1

    # Loop through each square position
    for row in range(board_size_h):
        for col in range(board_size_w):
            # Check if the current square is part of the frame
            is_in_frame = (
                row < frame_thickness or 
                col < frame_thickness or 
                row >= (board_size_h - frame_thickness) or 
                col >= (board_size_w - frame_thickness)
            )

            if is_in_frame:
                # Determine which color to use
                color_name = color1 if (row + col) % 2 == 0 else color2
                
                # Use a transparent tuple if "Transparent" is selected
                square_color = (0, 0, 0, 0) if color_name == "Transparent" else color_name

                # Calculate coordinates and draw the square
                x1, y1 = col * square_size, row * square_size
                x2, y2 = x1 + square_size, y1 + square_size
                draw.rectangle([x1, y1, x2, y2], fill=square_color)

    # Save the image to a temporary file for download
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
        image.save(temp_file.name)
        download_path = temp_file.name

    return image, download_path

# --- Create the Gradio Interface ---
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# Checkerboard Frame Generator")
    gr.Markdown("Create a checkerboard frame with a transparent center. Adjust the canvas, frame, and square sizes.")

    with gr.Row():
        width_slider = gr.Slider(minimum=200, maximum=4000, value=1080, step=10, label="Canvas Width (pixels)")
        height_slider = gr.Slider(minimum=200, maximum=4000, value=1080, step=10, label="Canvas Height (pixels)")

    with gr.Row():
        frame_thickness_slider = gr.Slider(minimum=1, maximum=20, value=2, step=1, label="Frame Thickness (in squares)")
        square_size_slider = gr.Slider(minimum=10, maximum=200, value=50, step=1, label="Square Size (pixels)")

    color_choices = ["Transparent", "White", "Black", "Gray", "Red", "Green", "Blue", "Yellow", "Purple", "Orange"]

    with gr.Row():
        dropdown_1 = gr.Dropdown(choices=color_choices, value="White", label="Color 1")
        dropdown_2 = gr.Dropdown(choices=color_choices, value="Black", label="Color 2")

    generate_button = gr.Button("Generate Frame")
    output_image = gr.Image(label="Generated Frame")
    download_button = gr.File(label="Download Image as PNG")

    generate_button.click(
        fn=create_checkerboard_frame,
        inputs=[width_slider, height_slider, frame_thickness_slider, square_size_slider, dropdown_1, dropdown_2],
        outputs=[output_image, download_button]
    )

if __name__ == "__main__":
    demo.launch()
