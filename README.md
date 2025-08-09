# Colorize-my-lineart-drawings

Simple tools for coloring black and white line drawings. The original image is never modified; a new colorized version is created instead.

## Usage

### Command line

```bash
python colorize.py path/to/lineart.png
```
The colorized image is saved alongside the original with ``_colorized`` appended to its name.

### Web app

Run the Gradio application to colorize drawings directly from the browser:

```bash
python app.py
```

Upload a line drawing and download the generated colorized copy.

## Installation

Install dependencies from ``requirements.txt``:

```bash
pip install -r requirements.txt
```
