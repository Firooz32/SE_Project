import tkinter as tk

def open_image():
    # Placeholder function to open an image
    print("Opening image...")

def save_image():
    # Placeholder function to save the edited image
    print("Saving image...")

def apply_filter(filter_name):
    global original_image, filtered_image
    if original_image:
        filtered_image = original_image.copy()
        if filter_name == "Grayscale":
            filtered_image = filtered_image.convert("L")
        elif filter_name == "Blur":
            filtered_image = filtered_image.filter(ImageFilter.BLUR)
        display_image(filtered_image)

# Create main application window
root = tk.Tk()
root.title("Ima-Mod")

# Create menu bar
menubar = tk.Menu(root)

# File menu
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=open_image)
filemenu.add_command(label="Save", command=save_image)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

# Edit menu
editmenu = tk.Menu(menubar, tearoff=0)
editmenu.add_command(label="Apply Filter", command=apply_filter)
menubar.add_cascade(label="Edit", menu=editmenu)

# Add menu bar to the root window
root.config(menu=menubar)

# Create toolbar (just buttons for simplicity)
toolbar = tk.Frame(root)
toolbar.pack(side=tk.TOP, fill=tk.X)

open_button = tk.Button(toolbar, text="Open", command=open_image)
open_button.pack(side=tk.LEFT, padx=2, pady=2)

save_button = tk.Button(toolbar, text="Save", command=save_image)
save_button.pack(side=tk.LEFT, padx=2, pady=2)

filter_button = tk.Button(toolbar, text="Apply Filter", command=apply_filter)
filter_button.pack(side=tk.LEFT, padx=2, pady=2)

# Canvas area for displayingg the image
canvas = tk.Canvas(root, bg="white", width=400, height=300)
canvas.pack()

# Run the applicatio
root.mainloop()



# File menu
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=open_image)
filemenu.add_command(label="Save", command=save_image)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

# Filter menu
filtermenu = tk.Menu(menubar, tearoff=0)
filtermenu.add_command(label="Grayscale", command=lambda: apply_filter("Grayscale"))
filtermenu.add_command(label="Blur", command=lambda: apply_filter("Blur"))
menubar.add_cascade(label="Filter", menu=filtermenu)

# Edit menu
editmenu = tk.Menu(menubar, tearoff=0)
editmenu.add_command(label="Apply Filter", command=apply_filter)
menubar.add_cascade(label="Edit", menu=editmenu)

# Add menu bar to the root window
root.config(menu=menubar)

# Create a label widget to display the image
label = tk.Label(root)
label.pack(padx=10, pady=10)


# Create toolbar (just buttons for simplicity)
toolbar = tk.Frame(root)
toolbar.pack(side=tk.TOP, fill=tk.X)

open_button = tk.Button(toolbar, text="Open", command=open_image)
open_button.pack(side=tk.LEFT, padx=2, pady=2)

save_button = tk.Button(toolbar, text="Save", command=save_image)
save_button.pack(side=tk.LEFT, padx=2, pady=2)

filter_button = tk.Button(toolbar, text="Apply Filter", command=apply_filter)
filter_button.pack(side=tk.LEFT, padx=2, pady=2)

# Canvas area for displaying the image
canvas = tk.Canvas(root, bg="white", width=400, height=300)
canvas.pack()

# Run the application
root.mainloop()
