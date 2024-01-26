# colorIndicator.py

import pyautogui
from PIL import ImageGrab
import tkinter as tk
import webcolors

def get_mouse_color():
    x, y = pyautogui.position()
    image = ImageGrab.grab(bbox=(x - 5, y - 5, x + 5, y + 5))
    color_rgb = image.getpixel((5, 5))
    return color_rgb

def rgb_to_color_name(rgb):
    try:
        color_name = webcolors.rgb_to_name(rgb)
        return color_name
    except ValueError:
        return None

def closest_color(rgb):
    min_colors = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - rgb[0]) ** 2
        gd = (g_c - rgb[1]) ** 2
        bd = (b_c - rgb[2]) ** 2
        min_colors[(rd + gd + bd)] = name
    return min_colors[min(min_colors.keys())]

def update_label():
    mouse_color_rgb = get_mouse_color()
    closest_color_name = closest_color(mouse_color_rgb)
    
    # Capitalize all text except for RGB values
    color_name = closest_color_name.capitalize() if closest_color_name else "Unknown"
    rgb_values = f"RGB Value: {mouse_color_rgb}"

    label.config(text=f"Color Name: {color_name}\n{rgb_values}")
    root.after(50, update_label)  # Update every 50 milliseconds

root = tk.Tk()
root.title("Color Indicator")

# Set the window to be always on top
root.attributes('-topmost', True)

label = tk.Label(root, font=("Arial", 12))
label.pack(pady=10)

root.geometry("300x100")
root.resizable(False, False)

root.after(50, update_label)  # Initial call to start updating

root.mainloop()
