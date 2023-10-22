import os
import uuid
from time import sleep

# CHANGE DIRECTORIES

downloads = "C:/default/download/directory/"
move_to = "C:/move/to/"

folders = ["Videos", "Images", "Web", "Audio files", "Executables", "Zip files", "Text files", "Scripts", "Docs"]

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
    ".app": "Executables",
    ".bat": "Executables",
    ".cmd": "Executables",
    ".zip": "Zip files",
    ".txt": "Text files",
    ".py": "Scripts",
    ".css": "Scripts",
    ".js": "Scripts",
    ".java": "Scripts",
    ".c": "Scripts",
    ".cpp": "Scripts",
    ".docx": "Docs",
    ".pptx": "Docs",
    ".xlsx": "Docs",
    ".one": "Docs"
    
}

def make_dirs():
    print(f"Checking for directories...")
    for i in folders:
        if i not in os.listdir(move_to):
            print(f"\n[{i}] does not exist, making directory.")
            os.makedirs(f"{move_to}/{i}")
            print(f"[{i}] directory has been made.\n")
    print("Directories are up to date.\n")

def main(num: int, messages_printed: set = set()):
    try:
        # List all files in the downloads directory
        downloaded_files = os.listdir(downloads)
        
        if not downloaded_files:
            # If no files are found and the message hasn't been printed yet, print it and add it to the set
            if "empty_downloads" not in messages_printed:
                print(f"Downloads folder is empty.")
                messages_printed.add("empty_downloads")
            sleep(5)
            return main(0, messages_printed)
        
        # Remove the flag from the set when files are found
        messages_printed.discard("empty_downloads")

        # Iterate through the downloaded files
        for downloaded_file in downloaded_files:
            for i in file_types:
                if downloaded_file.endswith(i):
                    # Your existing file processing logic
                    try:
                        if downloaded_file not in os.listdir(move_to+file_types[i]):
                            try:
                                os.replace(downloads+downloaded_file, move_to+file_types[i]+"/"+downloaded_file)
                            except PermissionError:
                                print(f"[{downloaded_file}] is opened somewhere else, cannot move.\n")
                                sleep(5)
                                return main(num+1, messages_printed)
                            print(f"Moved [{downloaded_file}] to [{move_to+file_types[i]}/]\n")
                            sleep(5)
                            return main(0, messages_printed)
                        else:
                            # If there's already a file with the same name
                            print(f"[{downloaded_file}] already exists in [{move_to+file_types[i]}]\n")
                            print(f"Making new name...\n")
                            new_name = uuid.uuid4().hex+"."+downloaded_file
                            print(f"[{downloaded_file}] has been renamed to [{new_name}]\n")
                            os.replace(downloads+downloaded_file, downloads+new_name)
                            return main(0, messages_printed)
                    except FileNotFoundError:
                        print(f"{file_types[i]} folder does not exist, making directory.\n")
                        os.mkdir(move_to+file_types[i])
                        print(f"Directory made\n")
                        if downloaded_file not in os.listdir(move_to+file_types[i]):
                            try:
                                os.replace(downloads+downloaded_file, move_to+file_types[i]+"/"+downloaded_file)
                            except PermissionError:
                                print(f"[{downloaded_file}]  is opened somewhere else.")
                                sleep(5)
                                return main(num+1, messages_printed)
                            print(f"Moved [{downloaded_file}] to {move_to+file_types[i]}/")
                            sleep(5)
                            return main(0, messages_printed)
                        else:
                            # If there's already a file with the same name
                            print(f"[{downloaded_file}] already exists in [{move_to+file_types[i]}]\n")
                            print(f"Renamed to {new_name}\n")
                            return main(num+1, messages_printed)
        try:
            os.replace(downloads+downloaded_file, move_to+"other/"+downloaded_file)
            sleep(5)
            return main(0, messages_printed)
        except FileNotFoundError:
            # Folder not found
            print(f"{file_types} folder does not exist, making directory.\n")
            os.makedirs(move_to+"other")
            os.replace(downloads+downloaded_file, move_to+"other/"+downloaded_file)
            print(f"Moved [{downloaded_file}] to [{move_to}/other]\n")
            sleep(5)
            return main(0, messages_printed)
        except PermissionError:
            print(f"[{downloaded_file}] is opened somewhere else, cannot move.\n")
            sleep(5)
            return main(num+1, messages_printed)
    
    except KeyboardInterrupt:
        print("\nExiting...")

make_dirs()

try:
    main(0)
except KeyboardInterrupt:
    print("\nExiting...")
