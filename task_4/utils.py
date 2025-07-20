import os
import shutil
import time


def is_path(directory_path: str) -> bool:
    """determines whether a directory exists"""
    print("\n>>> checking directory's existence...")
    time.sleep(1)
    return os.path.exists(directory_path)


def create_subdirectory(directory_path: str) -> None:
    """creates sub-directory based on file extension type"""
    extensions = [".pdf", ".docx", ".png", ".jpg"]
    file_names = fetch_directory_files(directory_path)

    if not file_names:
        print("\n\tError: empty directory")
        return 
    
    file_extensions = []

    for file_name in file_names:
        # extract file extensions
        print("\n>>> extracting file extensions...")
        time.sleep(1)
        extraction = os.path.splitext(file_name)
        file_extensions.append(extraction[1])
    
    # remove duplicates
    file_extensions = list(set(file_extensions))

    for file_extension in file_extensions:
        if (file_extension == ".docx" or file_extension == ".pdf"):
            if os.path.exists(f"{directory_path}/Documents"):
                continue
            print("\n>>> creating Documents directory...")
            time.sleep(1)
            os.mkdir(f"{directory_path}/Documents")
        elif (file_extension == ".png" or file_extension == ".jpg"):
            if os.path.exists(f"{directory_path}/Images"):
                continue
            print("\n>>> creating Images directory...")
            time.sleep(1)
            os.mkdir(f"{directory_path}/Images")



def fetch_directory_files(directory_path: str) -> list:
    """gets the file extension of each file in a directory"""
    print("\n>>> fecthing files in the directory...")
    time.sleep(1)
    
    file_names: list = os.listdir(directory_path)
    if len(file_names) == 0:
        return []
    
    sorted(file_names)

    return file_names


def oragnize_files(directory_path: str) -> None:
    """organize into sub-directories"""

    files = os.listdir(directory_path)
    extensions = [".pdf", ".docx", ".png", ".jpg"]
    documents = os.path.join(directory_path, "Documents")
    images = os.path.join(directory_path, "Images")

    for file_name in files:
        file_extension = os.path.splitext(file_name)[1]
        file_path = os.path.join(directory_path, file_name)

        if file_extension in extensions:
            if file_extension == ".docx" or file_extension == ".pdf":
                shutil.move(file_path, documents)
            elif file_extension == ".png" or file_extension == ".jpg":
                shutil.move(file_path, images)
        else:
            continue