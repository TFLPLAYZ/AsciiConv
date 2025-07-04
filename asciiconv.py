import argparse
import os
import sys
import time
from PIL import Image
import cv2
import numpy as np
from tkinter import Tk, filedialog
from tkinter.messagebox import showinfo
from tkinter import Tk, filedialog, Label, Entry, Button, BooleanVar, Checkbutton

ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']

class FileBrowser:
    def __init__(self):
        self.root = Tk()
        self.root.withdraw()
        self.file_path = None

    def browse_file(self):
        filetypes = (
            ('Media files', '*.jpg *.jpeg *.png *.bmp *.mp4 *.avi *.mov *.mkv'),
            ('All files', '*.*')
        )
        self.file_path = filedialog.askopenfilename(
            title='Select an image or video',
            initialdir='/',
            filetypes=filetypes
        )
        self.root.destroy()
        return self.file_path

def convert_image_to_ascii(image, output_width, color=False):
    aspect_ratio = image.height / image.width
    new_height = int(output_width * aspect_ratio * 0.5)
    resized_image = image.resize((output_width, new_height))
    
    if not color:
        resized_image = resized_image.convert('L')
    
    pixels = resized_image.getdata()
    ascii_str = ''
    
    for i, pixel in enumerate(pixels):
        if color:
            r, g, b = pixel[:3]
            brightness = 0.2126 * r + 0.7152 * g + 0.0722 * b
            char = ASCII_CHARS[min(int(brightness / 255 * (len(ASCII_CHARS)-1)), len(ASCII_CHARS)-1)]
            ascii_str += f'\033[38;2;{r};{g};{b}m{char}\033[0m'
        else:
            char = ASCII_CHARS[min(int(pixel / 255 * (len(ASCII_CHARS)-1)), len(ASCII_CHARS)-1)]
            ascii_str += char
        
        if (i + 1) % output_width == 0:
            ascii_str += '\n'
    
    return ascii_str

def handle_image(input_path, output_width, color):
    try:
        image = Image.open(input_path).convert('RGB')
        ascii_art = convert_image_to_ascii(image, output_width, color)
        print(ascii_art)
    except Exception as e:
        print(f"Error processing image: {e}")

def handle_video(input_path, output_width, color):
    try:
        cap = cv2.VideoCapture(input_path)
        fps = cap.get(cv2.CAP_PROP_FPS)
        
        while cap.isOpened():
            start_time = time.time()
            ret, frame = cap.read()
            if not ret:
                break
            
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(frame_rgb)
            ascii_frame = convert_image_to_ascii(image, output_width, color)
            
            os.system('cls' if os.name == 'nt' else 'clear')
            print(ascii_frame)
            
            processing_time = time.time() - start_time
            time.sleep(max(1/fps - processing_time, 0))
        
        cap.release()
    except Exception as e:
        print(f"Error processing video: {e}")

def main():
    # If no command line arguments, show file browser
    if len(sys.argv) == 1:
        browser = FileBrowser()
        input_path = browser.browse_file()
        if not input_path:
            print("No file selected")
            return
        
        # Create options dialog
        options_win = Tk()
        options_win.title("ASCII Converter Options")
        
        # Width selection
        width_label = Label(options_win, text="Output Width (characters):")
        width_label.pack()
        width_entry = Entry(options_win)
        width_entry.insert(0, "100")
        width_entry.pack()
        
        # Color selection
        color_var = BooleanVar()
        color_check = Checkbutton(options_win, text="Enable Color", variable=color_var)
        color_check.pack()
        
        def process():
            try:
                output_width = int(width_entry.get())
                color = color_var.get()
                options_win.destroy()
                
                if input_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                    handle_image(input_path, output_width, color)
                elif input_path.lower().endswith(('.mp4', '.avi', '.mov', '.mkv')):
                    handle_video(input_path, output_width, color)
                else:
                    showinfo("Error", "Unsupported file format")
            except ValueError:
                showinfo("Error", "Invalid width value")
        
        process_btn = Button(options_win, text="Convert", command=process)
        process_btn.pack()
        options_win.mainloop()
    else:
        # Original command line mode
        parser = argparse.ArgumentParser(description='Convert images/videos to ASCII art')
        parser.add_argument('--input', help='Input file path')
        parser.add_argument('--width', type=int, default=100, help='ASCII output width')
        parser.add_argument('--color', action='store_true', help='Enable color output')
        args = parser.parse_args()

        if not os.path.exists(args.input):
            print("Error: Input file does not exist")
            return

        if args.input.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            handle_image(args.input, args.width, args.color)
        elif args.input.lower().endswith(('.mp4', '.avi', '.mov', '.mkv')):
            handle_video(args.input, args.width, args.color)
        else:
            print("Error: Unsupported file format")

if __name__ == '__main__':
    main()
