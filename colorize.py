import cv2
import numpy as np
import os
from typing import Optional

def colorize_lineart(image_path: str, output_path: Optional[str] = None) -> str:
    """Colorize a line art drawing.

    The function reads a black and white line drawing from ``image_path`` and
    creates a new colorized image. The original file is left untouched.

    Args:
        image_path: Path to the input line art image.
        output_path: Optional path for the result. Defaults to ``<name>_colorized.png``.

    Returns:
        The path to the colorized image.
    """
    gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if gray is None:
        raise FileNotFoundError(f"Cannot load image {image_path}")

    white_mask = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)[1]
    num_labels, labels = cv2.connectedComponents(white_mask)

    color_img = np.ones((*gray.shape, 3), dtype=np.uint8) * 255
    for label in range(1, num_labels):
        mask = labels == label
        color = np.random.randint(0, 256, size=3, dtype=np.uint8)
        color_img[mask] = color

    line_mask = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)[1]
    color_img[line_mask == 255] = 0

    if output_path is None:
        root, _ = os.path.splitext(image_path)
        output_path = f"{root}_colorized.png"

    cv2.imwrite(output_path, color_img)
    return output_path


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Colorize a line art image")
    parser.add_argument("image", help="Path to the line art image")
    parser.add_argument("-o", "--output", help="Optional path for the colorized image")
    args = parser.parse_args()

    result_path = colorize_lineart(args.image, args.output)
    print(f"Saved colorized image to {result_path}")
