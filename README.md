
# Screen Capture Tool!

[gdfgdfd_animation](https://github.com/DARKSTONE-LABS/cardCap/assets/141037846/43894617-68ce-4b7a-b507-3a6038fb2d25)


This is a simple screen capture tool developed using Python's tkinter library for GUI and PIL (Python Imaging Library) for capturing and processing screen images. It allows users to capture screen animations, save them as GIF files, and provides a convenient interface for capturing.

## Features

- **Launch Viewfinder:** Start a semi-transparent viewfinder window that can be dragged around the screen.
- **Start Capture:** Begin capturing screen frames. Once started, it continuously captures screen frames until stopped.
- **Stop and Export:** Stop capturing, export captured frames as an animated GIF file, and specify the filename for saving.

## Prerequisites

- Python 3.x
- Tkinter (should be included in Python standard library)
- PIL (Python Imaging Library), can be installed via pip:

```bash
pip install pillow
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/screen-capture-tool.git
```

2. Navigate into the cloned directory:

```bash
cd screen-capture-tool
```

3. Run the application:

```bash
python screen_capture.py
```

## Usage

1. Launch the application.
2. Click on "Launch Viewfinder" to start the semi-transparent window.
3. Drag the viewfinder to the desired position.
4. Click on "Start Capture" to begin capturing screen frames.
5. After capturing, click on "Stop and Export" to save the captured frames as a GIF file.

## Example

![Example](example.gif)

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This tool is inspired by various screen capture applications available online.
- Thanks to the contributors of Tkinter and PIL libraries for providing the necessary tools for GUI development and image processing in Python.
