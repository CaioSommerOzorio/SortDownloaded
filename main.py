import os
import sys
from time import sleep
# CHANGE DIRECTORIES
downloads = "Default/downloads/folder"
move_to = "Where/files/will/be/stored"
file_types = {
    ".mp4": "Videos", 
    ".mov": "Videos", 
    ".webm": "Videos", 
    ".mkv": "Videos", 
    ".avi": "Videos", 
    ".asf": "Videos", 
    ".mpeg": "Videos", 
    ".png": "Images",
    ".jpeg": "Images",
    ".webp": "Images",
    ".jpg": "Images",
    ".ico": "Images",
    ".pdf": "Web",
    ".html": "Web",
    ".mp3": "Audio files",
    ".wav": "Audio files",
    ".ogg": "Audio files",
    ".exe": "Executables",
    ".zip": "Zip files",
    ".txt": "Text files",
    ".py": "Scripts",
    ".css": "Scripts",
    ".js": "Scripts",
    ".java": "Scripts",
    ".c": "Scripts",
    ".cpp": "Scripts"
}
def recurse(num):
    # Remove sleep function for cleaning up all files
    sleep(5)
    # Checks if file is still being downloaded
    if os.listdir(downloads)[0].endswith(".crdownload"):
        return recurse(num+1)
    try:
        # Declare downloaded file
        downloaded_file = os.listdir(downloads)[0+num]
    except IndexError:
        # If downloads folder is empty
        return recurse(0)
    for i in file_types:
        if downloaded_file.endswith(i):
            if downloaded_file not in os.listdir(move_to+file_types[i]):
                os.replace(downloads+downloaded_file, move_to+file_types[i]+"/"+downloaded_file)
                print("Successfull")
                print(f"Moved {downloaded_file} to {move_to+file_types[i]}/")
                return recurse(0)
            else:
                # If there's already a file with the same name
                print(f"'{downloaded_file}' already exists in '{move_to+file_types[i]}'")
                return recurse(num+1)
    print("Does not match with anything, moving to other")
    os.replace(downloads+downloaded_file, move_to+"other/"+downloaded_file)
    return recurse(0)
        

recurse(0)
