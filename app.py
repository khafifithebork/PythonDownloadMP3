import os
from tkinter import Tk, Label, Entry, Button, filedialog, messagebox
from tempfile import TemporaryDirectory
from utils.downloader import download_audio
from utils.player import play_audio

def download_and_play():
    """
    Downloads audio from the given URL and plays it.
    """
    youtube_url = url_entry.get()
    if not youtube_url.strip():
        messagebox.showerror("Error", "Please enter a valid YouTube URL.")
        return
    
    with TemporaryDirectory() as temp_dir:
        try:
            status_label.config(text="Downloading audio...")
            audio_file = download_audio(youtube_url, temp_dir)
            status_label.config(text="Download complete. Playing audio...")
            play_audio(audio_file)
            status_label.config(text="Done.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            status_label.config(text="Error occurred.")

# Create the GUI window
root = Tk()
root.title("YouTube Audio Player")
root.geometry("800x400")

# Add a label and text entry for the YouTube URL
Label(root, text="Enter YouTube URL:").pack(pady=5)
url_entry = Entry(root, width=50)
url_entry.pack(pady=5)

# Add a button to start the process
play_button = Button(root, text="Download & Play", command=download_and_play)
play_button.pack(pady=10)

# Add a status label
status_label = Label(root, text="")
status_label.pack(pady=5)

# Run the GUI event loop
root.mainloop()

