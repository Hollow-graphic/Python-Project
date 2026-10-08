import os
import shutil
import glob

music_files = glob.glob(os.path.join(r"C:\Users\Adam\Desktop\Shortcut\Music", "*.mp3"))

for i in music_files:
    shutil.copy2(i, i.replace("\\Music", "\\Music\\audio"))