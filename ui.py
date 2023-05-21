import tkinter as tk
from LSB import *
import tkinter.simpledialog as simpledialog
from compare import *
from image import *
from compare_image import *
from echo import *
import tkinter as tk
from tkinter import filedialog

# Function definitions
def function1():
    root = tk.Tk()
    root.withdraw()

    # Open a file dialog box and allow user to select a file
    file_path = filedialog.askopenfilename()
    encode_str = file_path
    message_str = simpledialog.askstring("Input", "Enter the message to be Encoded:")
    if encode_str:
        print(f"Function 1 executed with input: {encode_str} and {message_str}")
        encode=encode_str
        message=message_str
        encode_LSB(encode,message)
        decode_LSB("encoded.wav")
        compare()
    else:
        print("Input cannot be empty.")
    
def function2():
    root = tk.Tk()
    root.withdraw()

    # Open a file dialog box and allow user to select a file
    file_path = filedialog.askopenfilename()

    encode_str = file_path
    message_str = simpledialog.askstring("Input", "Enter the message to be Encoded:")
    encode_image(encode_str,message_str)
    print(decode_image("encoded_image.png"))
    compare_images("E:/Study Lectures notes/3rd Year/Sem 6/CS/Course Project/hello.png","E:/Study Lectures notes/3rd Year/Sem 6/CS/Course Project/encoded_image.png")
    
    
def function3():
    message = 'Hello, world!'
    input_file = 'trial.wav'
    output_file = 'output_echo.wav'
    encode_echo(message, input_file, output_file)
    
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
title_label = tk.Label(window, text="Welcome to Steganography Techniques", font=("Arial", 20), pady=20)
title_label.pack()

# Add a frame to contain the buttons with margin
button_frame = tk.Frame(window, bg="#f0f0f0", pady=20, padx=50)
button_frame.pack()

# Add the buttons
button1 = tk.Button(button_frame, text="Audio LSB Technique", font=("Arial", 16), padx=20, pady=10, command=function1)
button1.grid(row=0, column=0)
button2 = tk.Button(button_frame, text="Image Technique", font=("Arial", 16), padx=40, pady=10, command=function2)
button2.grid(row=1, column=0)

button3 = tk.Button(button_frame, text="Audio Echo Technique", font=("Arial", 16), padx=20, pady=10, command=function3)
button3.grid(row=2, column=0)
button4 = tk.Button(button_frame, text="Video Steganography", font=("Arial", 16), padx=20, pady=10, command=function3)
button4.grid(row=3, column=0)


# Center the buttons
button_frame.pack_propagate(0)
button_frame.update_idletasks()
button_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Start the main loop
window.mainloop()
