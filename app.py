import gradio as gr
import numpy as np
from PIL import Image
from tempfile import NamedTemporaryFile
import os

from colorize import colorize_lineart


def interface(image: np.ndarray) -> Image.Image:
    """Gradio interface function that returns a colorized version of the image."""
    with NamedTemporaryFile(suffix=".png", delete=False) as tmp:
        Image.fromarray(image).save(tmp.name)
        result_path = colorize_lineart(tmp.name)
        result = Image.open(result_path).convert("RGB")
    os.remove(tmp.name)
    os.remove(result_path)
    return result


demo = gr.Interface(
    fn=interface,
    inputs=gr.Image(type="numpy"),
    outputs="image",
    title="Line Art Colorizer",
    description="Upload a line drawing to receive a colorized copy. The original image is never modified."
)


if __name__ == "__main__":
    demo.launch()
