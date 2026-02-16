import tkinter as tk

def on_button_click():
    label.config(text="Button Clicked!")

# Create the main window
root = tk.Tk()
root.title("Widgets Demo")

# Add a label
label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 16))
label.pack()

# Add a button
button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack()

# Run the application
root.mainloop()
