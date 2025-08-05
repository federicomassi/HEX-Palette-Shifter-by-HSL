import tkinter as tk
from tkinter import filedialog, messagebox
import re
import os
from colorsys import rgb_to_hls, hls_to_rgb


def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i + 2], 16) / 255.0 for i in (0, 2, 4))


def rgb_to_hex(rgb):
    return "#" + "".join(f"{int(round(c * 255)):02x}" for c in rgb)


def shift_hue(hex_color, hue_shift, lightness_shift=0, saturation_shift=0):
    r, g, b = hex_to_rgb(hex_color)
    h, l, s = rgb_to_hls(r, g, b)
    h = (h + hue_shift / 360.0) % 1.0
    l = max(0.0, min(1.0, l + lightness_shift))
    s = max(0.0, min(1.0, s + saturation_shift))
    r, g, b = hls_to_rgb(h, l, s)
    return rgb_to_hex((r, g, b))


class ColorTransformerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("HEX to HSL palette shifter")
        self.root.geometry("1000x400")

        self.filename = None
        self.original_hex_colors = []
        self.transformed_colors = []

        tk.Button(root, text="Load File", command=self.load_file).pack(pady=5)
        
        self.canvas_orig = tk.Canvas(root, height=50)
        self.canvas_orig.pack()

        self.hue_slider = tk.Scale(root, from_=-180, to=180, orient=tk.HORIZONTAL, label="Shift Hue (degrees)", command=self.apply_shift)
        self.hue_slider.pack(fill=tk.X, padx=10)

        self.lightness_slider = tk.Scale(root, from_=-0.5, to=0.5, resolution=0.01, orient=tk.HORIZONTAL, label="Shift Luminosity (from -0.5 to +0.5)", command=self.apply_shift)
        self.lightness_slider.pack(fill=tk.X, padx=10)

        self.saturation_slider = tk.Scale(root, from_=-0.5, to=0.5, resolution=0.01, orient=tk.HORIZONTAL, label="Shift Saturation (from -0.5 to +0.5)", command=self.apply_shift)
        self.saturation_slider.pack(fill=tk.X, padx=10)

        # tk.Button(root, text="Apply Shift", command=self.apply_shift).pack(pady=5)

        self.canvas_transformed = tk.Canvas(root, height=50)
        self.canvas_transformed.pack()

        tk.Button(root, text="Save File", command=self.save_new_file).pack(pady=5)

    def load_file(self):
        self.filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt *.css *.html *.json *.js"), ("All files", "*.*")])
        if not self.filename:
            return

        with open(self.filename, 'r', encoding='utf-8') as f:
            self.file_content = f.read()

        self.original_hex_colors = list(set(re.findall(r"#[0-9a-fA-F]{6}", self.file_content)))
        self.draw_palette(self.canvas_orig, self.original_hex_colors)

    def draw_palette(self, canvas, colors):
        canvas.delete("all")
        width = canvas.winfo_width() or canvas.winfo_reqwidth()
        n = len(colors)
        if n == 0:
            return
        bar_width = width // n
        for i, color in enumerate(colors):
            canvas.create_rectangle(i * bar_width, 0, (i + 1) * bar_width, 40, fill=color, outline=color)

    def apply_shift(self, *args):
        hue_shift = self.hue_slider.get()
        lightness_shift = self.lightness_slider.get()
        saturation_shift = self.saturation_slider.get()
        self.transformed_colors = [shift_hue(color, hue_shift, lightness_shift, saturation_shift) for color in self.original_hex_colors]
        self.draw_palette(self.canvas_transformed, self.transformed_colors)

    def save_new_file(self):
        if not self.filename or not self.transformed_colors:
            messagebox.showerror("Error", "Load a file and apply shifts before saving.")
            return

        new_content = self.file_content
        for orig, new in zip(self.original_hex_colors, self.transformed_colors):
            new_content = re.sub(re.escape(orig), new, new_content)

        base, ext = os.path.splitext(self.filename)
        lig = self.lightness_slider.get()
        sat = self.saturation_slider.get()
        hue = self.hue_slider.get()
        new_filename = f"{base}_shift_{hue}_{sat}_{lig}{ext}"

        with open(new_filename, 'w', encoding='utf-8') as f:
            f.write(new_content)

        messagebox.showinfo("Saved", f"File saved as:\n{new_filename}")


if __name__ == '__main__':
    root = tk.Tk()
    app = ColorTransformerApp(root)
    root.mainloop()
