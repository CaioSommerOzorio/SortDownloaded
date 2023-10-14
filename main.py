import os
from time import sleep

# CHANGE DIRECTORIES AND USER NAME.
downloads = "C:/Users/CHANGE/Downloads/"
move_to = "C:/Users/CHANGE/Desktop/CHANGE/"

# Feel free to add any more file types, values are the names of the folder in which the file types are stored.
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
    ".pdf": "Web",
    ".html": "Web",
    ".mp3": "Audio files",
    ".wav": "Audio files",
    ".ogg": "Audio files",
    ".exe": "Executables",
    ".zip": "Zip files"
}
# Makes program work, coded this 5 minutes ago and have no idea what's going on.
def recurse():
    # So it doesn't recurst infinitely, remove/comment to sort a large amount.
    sleep(7)
    try:
        for i in file_types:
            # Checks if file ends with extension
            if os.listdir(downloads)[0].endswith(i):
                # Uncomment below for debugging
                #print(os.listdir(downloads)[0]+ " ends with "+i)
                # Moves file from downloads/filename.ext, to directory/filetype/filename.ext
                os.replace(downloads+os.listdir(downloads)[0], move_to+file_types[i]+"/"+os.listdir(downloads)[0])
                return recurse()
        # If file has no matching extensions, move to other.
        os.replace(downloads+os.listdir(downloads)[0], move_to+"other/"+os.listdir(downloads)[0])
        return recurse()
    # Temporary fix, will add if statement to check for files in dir
    except IndexError:
        return recurse()    
        

recurse()
