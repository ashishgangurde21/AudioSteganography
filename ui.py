import tkinter as tk
from lsb import *
import tkinter.simpledialog as simpledialog

# Function definitions
def function1():
    encode_str = simpledialog.askstring("Input", "Enter a The WAV file to be encoded:")
    message_str = simpledialog.askstring("Input", "Enter the message to be Encoded:")
    if encode_str:
        print(f"Function 1 executed with input: {encode_str} and {message_str}")
        encode=encode_str
        message=message_str
        encode_LSB(encode,message)
        decode_LSB("encoded.wav")
        
        
    else:
        print("Input cannot be empty.")
    
def function2():
    print("Function 2 executed.")
    
def function3():
    print("Function 3 executed.")
    
def function4():
    print("Function 4 executed.")

# Create the main window
window = tk.Tk()

# Set the window title
window.title("Welcome to Steganography Techniques")

# Set the window size
window.geometry("500x400")

# Set the window background color
window.config(bg="#f0f0f0")

# Add a title label
title_label = tk.Label(window, text="Welcome to Steganography techniques", font=("Arial", 20), pady=20)
title_label.pack()

# Add a frame to contain the buttons with margin
button_frame = tk.Frame(window, bg="#f0f0f0", pady=20, padx=50)
button_frame.pack()

# Add the buttons
button1 = tk.Button(button_frame, text="Function 1", font=("Arial", 16), padx=20, pady=10, command=function1)
button1.grid(row=0, column=0)

button2 = tk.Button(button_frame, text="Function 2", font=("Arial", 16), padx=20, pady=10, command=function2)
button2.grid(row=0, column=2)

button3 = tk.Button(button_frame, text="Function 3", font=("Arial", 16), padx=20, pady=10, command=function3)
button3.grid(row=1, column=0)

button4 = tk.Button(button_frame, text="Function 4", font=("Arial", 16), padx=20, pady=10, command=function4)
button4.grid(row=1, column=2)

# Center the buttons
button_frame.pack_propagate(0)
button_frame.update_idletasks()
button_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Start the main loop
window.mainloop()
