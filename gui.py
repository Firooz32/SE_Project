import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFilter

def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
    if file_path:
        global original_image
        original_image = Image.open(file_path)
        original_image.thumbnail((300, 300))  # Resize the image to fit in the window
        display_image(original_image)

def save_image():
    global original_image, filtered_image
    if filtered_image:
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            filtered_image.save(file_path)


def display_image(image):
    global label
    photo = ImageTk.PhotoImage(image)
    label.config(image=photo)
    label.image = photo  # Keep a reference to avoid garbage collection


def apply_filter(filter_name):
    global original_image, filtered_image
    if original_image:
        filtered_image = original_image.copy()
        if filter_name == "Grayscale":
            filtered_image = filtered_image.convert("L")
        elif filter_name == "Blur":
            filtered_image = filtered_image.filter(ImageFilter.BLUR)
        display_image(filtered_image)
        
def reset_image():
    global displayed_image
    if original_image:
        displayed_image = original_image.copy()
        display_image(displayed_image)       

# Create main application window
root = tk.Tk()
root.title("Ima-Mod")

# Create menu bar
menubar = tk.Menu(root)

# File menu
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Open Image", command=open_image)
filemenu.add_command(label="Save Image", command=save_image)
menubar.add_cascade(label="File", menu=filemenu)

#Reset button display
reset_button = tk.Button(root, text="Reset", command=reset_image)
reset_button.pack(pady=5)

# Filter menu
filtermenu = tk.Menu(menubar, tearoff=0)
filtermenu.add_command(label="Grayscale", command=lambda: apply_filter("Grayscale"))
filtermenu.add_command(label="Blur", command=lambda: apply_filter("Blur"))
menubar.add_cascade(label="Filter", menu=filtermenu)

# Add menu bar to the root window
root.config(menu=menubar)

# Add menu bar to the root window
root.config(menu=menubar)

# Create a label widget to display the image
label = tk.Label(root)
label.pack(padx=10, pady=10)

# Global variables to store the original and filtered images
original_image = None
filtered_image = None

# Run the application
root.mainloop()
