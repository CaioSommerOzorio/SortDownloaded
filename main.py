import os
import uuid
from colorama import init, Fore
from time import sleep
init()
# CHANGE DIRECTORIES

downloads = "C:/Default/download/directory/"
move_to = "C:/Move/to/folder/"

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
                        print(Fore.BLUE + downloaded_file + Fore.RED + " is opened somewhere else.")
                        sleep(5)
                        return main(num+1)
                    print(f"{Fore.GREEN}Moved "+ Fore.BLUE + downloaded_file + f"{Fore.GREEN}to {Fore.GREEN}[{move_to+file_types[i]}/]")
                    sleep(5)
                    return main(0)
                else:
                    # If there's already a file with the same name
                    print(f"{Fore.BLUE}[{downloaded_file}] {Fore.RED}already exists in {Fore.BLUE}[{move_to+file_types[i]}]")
                    print(f"{Fore.GREEN}Making new name...")
                    new_name = uuid.uuid4().hex+"."+downloaded_file
                    print(f"{Fore.BLUE}[{downloaded_file}]{Fore.GREEN} has been renamed to {Fore.BLUE}[{new_name}]")
                    os.replace(downloads+downloaded_file, downloads+new_name)
                    return main(0)
            except FileNotFoundError:
                print(f"{Fore.BLUE}{file_types[i]}{Fore.RED} folder does not exist, making directory.")
                os.mkdir(move_to+file_types[i])
                print(f"{Fore.GREEN}Directory made")
                if downloaded_file not in os.listdir(move_to+file_types[i]):
                    try:
                        os.replace(downloads+downloaded_file, move_to+file_types[i]+"/"+downloaded_file)
                    except PermissionError:
                        print(f"{Fore.BLUE}[{downloaded_file}] {Fore.GREEN}opened somewhere else.")
                        sleep(5)
                        return main(num+1)
                    print(f"{Fore.GREEN}Moved {Fore.BLUE}[{downloaded_file}]{Fore.GREEN} to {Fore.BLUE}{move_to+file_types[i]}/")
                    sleep(5)
                    return main(0)
                else:
                    # If there's already a file with the same name
                    print(f"{Fore.Blue}[{downloaded_file}] {Fore.RED}already exists in {Fore.BLUE}[{move_to+file_types[i]}]")
                    
                    print("Renamed to ")
                    return main(num+1)
    try:
        os.replace(downloads+downloaded_file, move_to+"other/"+downloaded_file)
        sleep(5)
        return main(0)
    except FileNotFoundError:
        # Folder not found
        print(f"{Fore.BLUE}{file_types}{Fore.RED} folder does not exist, making directory.")
        os.makedirs(move_to+"other")
        os.replace(downloads+downloaded_file, move_to+"other/"+downloaded_file)
        print(Fore.GREEN + "Moved " + Fore.BLUE + f"[{downloaded_file}]" + Fore.GREEN + "to {move_to}/other")
        sleep(5)
        return main(0)
    except PermissionError:
        print(Fore.BLUE + f"[{downloaded_file}]" + Fore.RED + " is opened somewhere else.")
        sleep(5)
        return main(num+1)
    

try:
    main(0)
except KeyboardInterrupt:
    print(Fore.RED + "\nExiting...")
