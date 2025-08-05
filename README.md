# HEX Palette Shifter by HSL

A simple Tkinter-based tool to edit and transform color palettes defined in HEX format.  
This application is useful for converting files containing HEX color codes (e.g., CTkinter JSON themes, CSS files, or templates) by **shifting hue, saturation, and lightness** uniformly across the palette.

## Features

-  📂 Load any text-based file (e.g., `.txt`, `.css`, `.html`, `.json`, `.js`) with HEX colors in the format `#RRGGBB`
-  🎨 Automatically extracts all unique HEX colors and displays them as a palette
-  🎚️ Real-time sliders to adjust:
   -  **Hue** (`-180°` to `+180°`)
   -  **Saturation** (`-0.5` to `+0.5`)
   -  **Lightness** (`-0.5` to `+0.5`)
-  🖼️ Visual preview of the transformed palette
-  💾 Save the modified file with a new name, preserving the original format and structure

## Installation

This is a standalone Python script. Requirements:

-  Python 3.x

No external libraries are needed — only the standard library.

## Usage

1. Run the script:

   ```bash
   python hex_palette_shifter_by_hsl.py
   ```

2. Click **Load File** to select a file containing HEX colors.

3. Adjust the **Hue**, **Saturation**, and **Lightness** sliders to preview the transformation in real time.

4. Click **Save File** to generate a new version of the file with updated color codes.

   The output filename will be suffixed with the applied shift values, e.g.:

   ```
   theme_shift_30_0.2_-0.1.css
   ```

## Example Use Cases

-  Adjusting the color tone of a **CTkinter theme**
-  Recoloring small **CSS snippets** or **code snippets**
-  Creating **multiple color variants** of a visual template

## License

This project is licensed under the **GNU GPL 3.0 License**.

---

Made with ❤️ using Python and Tkinter.
