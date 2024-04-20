import os
def list_files_in_directory(directory_path):
    """
    Lists files in directory
    """
    try:
        files = os.listdir(directory_path)
        return files
    except FileNotFoundError:
        return None