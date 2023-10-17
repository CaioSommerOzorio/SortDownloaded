import os
import sys
from time import sleep

# CHANGE DIRECTORIES

downloads = "C:/Users/farof/Downloads/"
move_to = "C:/Users/farof/Onedrive/Desktop/Downloaded/"

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

def main(num: int):
    # Checks if file is still being downloaded
    if os.listdir(downloads)[0].endswith(".crdownload"):
        print("File has not finished downloading")
        sleep(5)
        return main(num+1)
    try:
        # Declare downloaded file
        downloaded_file = os.listdir(downloads)[0+num]
    except IndexError:
        # If downloads folder is empty
        sleep(5)
        return main(0)
    for i in file_types:
        if downloaded_file.endswith(i):
            try:
                if downloaded_file not in os.listdir(move_to+file_types[i]):
                    try:
                        os.replace(downloads+downloaded_file, move_to+file_types[i]+"/"+downloaded_file)
                    except PermissionError:
                        print("File opened somewhere else.")
                        sleep(5)
                        return main(+1)
                    print(f"Moved {downloaded_file} to {move_to+file_types[i]}/")
                    sleep(5)
                    return main()
                else:
                    # If there's already a file with the same name
                    print(f"'{downloaded_file}' already exists in '{move_to+file_types[i]}'")
                    sleep(5)
                    return main(num+1)
            except FileNotFoundError:
                print(f"{file_types[i]} folder does not exist, making directory.")
                os.mkdir(move_to+file_types[i])
                print("Directory made")
                if downloaded_file not in os.listdir(move_to+file_types[i]):
                    try:
                        os.replace(downloads+downloaded_file, move_to+file_types[i]+"/"+downloaded_file)
                    except PermissionError:
                        print("File opened somewhere else.")
                        sleep(5)
                        return main(num+1)
                    print(f"Moved [{downloaded_file}] to {move_to+file_types[i]}/")
                    sleep(5)
                    return main(0)
                else:
                    # If there's already a file with the same name
                    print(f"[{downloaded_file}] already exists in '{move_to+file_types[i]}'")
                    return main(num+1)
    try:
        os.replace(downloads+downloaded_file, move_to+"other/"+downloaded_file)
        sleep(5)
        return main(0)
    except FileNotFoundError:
        # Folder not found
        print(f"{file_types} folder does not exist, making directory.")
        os.makedirs(move_to+"other")
        os.replace(downloads+downloaded_file, move_to+"other/"+downloaded_file)
        print(f"Moved [{downloaded_file}] to {move_to}/other")
        sleep(5)
        return main(0)
    except PermissionError:
        print(f"[{downloaded_file}] is opened somewhere else.")
        sleep(5)
        return main(num+1)
    
try:
    main(0)
except KeyboardInterrupt:
    print("\nExiting...")
