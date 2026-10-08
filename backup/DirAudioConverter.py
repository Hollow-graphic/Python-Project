import moviepy.editor 
from tkinter.filedialog import *
import os
import glob

dir = r"C:\Users\Adam\Desktop\Shortcut\Music"
audio_dir = r"C:\Users\Adam\Desktop\Shortcut\Music\audio"

music_files = glob.glob(os.path.join(r"C:\Users\Adam\Desktop\Shortcut\Music", "*.mp4"))

for file in music_files:
    if os.path.exists(file.replace("\\Music", "\\Music\\audio")):
        continue
    
    print(file)
    save_path = file.replace(".mp4", ".mp3")
    file = moviepy.editor.VideoFileClip(file)
    audio=file.audio
    save_path = save_path.replace("\\Music", "\\Music\\audio")
    audio.write_audiofile(save_path)