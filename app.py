import gradio as gr
from PIL import Image, ImageDraw
import tempfile

# Define a dictionary of preset canvas sizes (width, height)
PRESET_SIZES = {
    "Square (1080x1080)": (1080, 1080),
    "Widescreen (1920x1080)": (1920, 1080),
    "Portrait (1080x1920)": (1080, 1920),
    "Classic TV (1200x900)": (1200, 900),
}

def create_checkerboard_frame(preset_name, frame_thickness, square_size, color1, color1_transparent, color2, color2_transparent):
    """
    Generates a checkerboard frame on a transparent canvas.
    """
    # Get the image dimensions from the selected preset
    image_width, image_height = PRESET_SIZES[preset_name]

    # Calculate how many squares will fit in the canvas
    cols = int(image_width / square_size) + 1
    rows = int(image_height / square_size) + 1

    # Create a new blank image in RGBA mode to support transparency
    image = Image.new("RGBA", (image_width, image_height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)

    # Determine the actual colors to use
    final_color1 = (0, 0, 0, 0) if color1_transparent else color1
    final_color2 = (0, 0, 0, 0) if color2_transparent else color2

    # Loop through each square position
    for r in range(rows):
        for c in range(cols):
            # *** CORE LOGIC: Check if the current square is part of the frame ***
            is_frame = r < frame_thickness or r >= rows - frame_thickness or \
                       c < frame_thickness or c >= cols - frame_thickness
            
            if is_frame:
                # Determine which color to use for the current square
                square_color = final_color1 if (r + c) % 2 == 0 else final_color2
                
                # Calculate the coordinates of the square
                x1 = c * square_size
                y1 = r * square_size
                x2 = x1 + square_size
                y2 = y1 + square_size
                
                # Draw the rectangle, but only if the color isn't fully transparent
                if square_color[3] != 0 if isinstance(square_color, tuple) else True:
                    draw.rectangle([x1, y1, x2, y2], fill=square_color)

    # Save the image to a temporary file to make it downloadable
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
        image.save(temp_file.name)
        download_path = temp_file.name

    return image, download_path

# --- Create the Gradio Interface ---
with gr.Blocks(theme=gr.themes.Soft(primary_hue="pink", secondary_hue="orange")) as demo:
    gr.Markdown("# Checkerboard Frame Generator")
    gr.Markdown("Create a custom checkerboard frame. The center will remain transparent. The image updates automatically as you change the settings.")

    with gr.Row():
        with gr.Column(scale=2):
            # Input controls
            preset_dropdown = gr.Dropdown(choices=list(PRESET_SIZES.keys()), value="Square (1080x1080)", label="Canvas Size Preset")
            frame_thickness_slider = gr.Slider(minimum=1, maximum=20, value=3, step=1, label="Frame Thickness (in squares)")
            square_size_slider = gr.Slider(minimum=10, maximum=200, value=50, step=1, label="Square Size (pixels)")
            
            with gr.Row():
                color_picker_1 = gr.ColorPicker(value="#6b7280", label="Color 1")
                transparent_cb_1 = gr.Checkbox(label="Transparent", value=False)
            with gr.Row():
                color_picker_2 = gr.ColorPicker(value="#d1d5db", label="Color 2")
                transparent_cb_2 = gr.Checkbox(label="Transparent", value=False)
            
            download_button = gr.File(label="Download Image as PNG", interactive=False)

        with gr.Column(scale=3):
            # Output display
            output_image = gr.Image(label="Generated Frame", interactive=False, height=500)

    # List of all input components
    inputs = [
        preset_dropdown, 
        frame_thickness_slider, 
        square_size_slider, 
        color_picker_1,
        transparent_cb_1,
        color_picker_2,
        transparent_cb_2
    ]

    # Link the controls to the function. The 'live=True' makes it update automatically.
    for component in inputs:
        component.change(
            fn=create_checkerboard_frame,
            inputs=inputs,
            outputs=[output_image, download_button],
            # api_name="generate" # This line is not needed for the UI to work
        )

if __name__ == "__main__":
    demo.launch()
