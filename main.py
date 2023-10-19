import os
import uuid
from colorama import init, Fore
from time import sleep
init()
# CHANGE DIRECTORIES

downloads = "C:/default/downloads/directory/"
move_to = "C:/directory/files/will/be/moved/to"

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
    print(f"{Fore.GREEN}Checking for directories...")
    for i in folders:
        if i not in os.listdir(move_to):
            print(f"\n{Fore.BLUE}[{i}]{Fore.RED} does not exist, making directory.")
            os.makedirs(f"{move_to}/{i}")
            print(f"{Fore.BLUE}[{i}]{Fore.GREEN} directory has been made.\n")
    print("Directories are up to date.\n")

def main(num: int, messages_printed: set = set()):
    try:
        # List all files in the downloads directory
        downloaded_files = os.listdir(downloads)
        
        if not downloaded_files:
            # If no files are found and the message hasn't been printed yet, print it and add it to the set
            if "empty_downloads" not in messages_printed:
                print(f"{Fore.RED}Downloads folder is empty.")
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
                                print(f"{Fore.BLUE}[{downloaded_file}]{Fore.RED} is opened somewhere else, cannot move.\n")
                                sleep(5)
                                return main(num+1, messages_printed)
                            print(f"{Fore.GREEN}Moved {Fore.BLUE}[{downloaded_file}]{Fore.GREEN} to {Fore.BLUE}[{move_to+file_types[i]}/]\n")
                            sleep(5)
                            return main(0, messages_printed)
                        else:
                            # If there's already a file with the same name
                            print(f"{Fore.BLUE}[{downloaded_file}] {Fore.RED}already exists in {Fore.BLUE}[{move_to+file_types[i]}]\n")
                            print(f"{Fore.GREEN}Making new name...\n")
                            new_name = uuid.uuid4().hex+"."+downloaded_file
                            print(f"{Fore.BLUE}[{downloaded_file}]{Fore.GREEN} has been renamed to {Fore.BLUE}[{new_name}]\n")
                            os.replace(downloads+downloaded_file, downloads+new_name)
                            return main(0, messages_printed)
                    except FileNotFoundError:
                        print(f"{Fore.BLUE}{file_types[i]}{Fore.RED} folder does not exist, making directory.\n")
                        os.mkdir(move_to+file_types[i])
                        print(f"{Fore.GREEN}Directory made\n")
                        if downloaded_file not in os.listdir(move_to+file_types[i]):
                            try:
                                os.replace(downloads+downloaded_file, move_to+file_types[i]+"/"+downloaded_file)
                            except PermissionError:
                                print(f"{Fore.BLUE}[{downloaded_file}] {Fore.GREEN} is opened somewhere else.")
                                sleep(5)
                                return main(num+1, messages_printed)
                            print(f"{Fore.GREEN}Moved {Fore.BLUE}[{downloaded_file}]{Fore.GREEN} to {Fore.BLUE}{move_to+file_types[i]}/")
                            sleep(5)
                            return main(0, messages_printed)
                        else:
                            # If there's already a file with the same name
                            print(f"{Fore.Blue}[{downloaded_file}] {Fore.RED}already exists in {Fore.BLUE}[{move_to+file_types[i]}]\n")
                            print(f"Renamed to {new_name}\n")
                            return main(num+1, messages_printed)
        try:
            os.replace(downloads+downloaded_file, move_to+"other/"+downloaded_file)
            sleep(5)
            return main(0, messages_printed)
        except FileNotFoundError:
            # Folder not found
            print(f"{Fore.BLUE}{file_types}{Fore.RED} folder does not exist, making directory.\n")
            os.makedirs(move_to+"other")
            os.replace(downloads+downloaded_file, move_to+"other/"+downloaded_file)
            print(f"{Fore.GREEN}Moved {Fore.BLUE}[{downloaded_file}]{Fore.GREEN} to {Fore.BLUE}[{move_to}/other]\n")
            sleep(5)
            return main(0, messages_printed)
        except PermissionError:
            print(f"{Fore.BLUE}[{downloaded_file}]{Fore.RED} is opened somewhere else, cannot move.\n")
            sleep(5)
            return main(num+1, messages_printed)
    
    except KeyboardInterrupt:
        print(Fore.RED + "\nExiting...")

make_dirs()

try:
    main(0)
except KeyboardInterrupt:
    print(Fore.RED + "\nExiting...")
