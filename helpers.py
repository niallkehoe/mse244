import os

def fetch_and_sort_filenames(directory, prefix):
    """
    Fetches all filenames in the specified directory with the given prefix and sorts them.

    Parameters:
    directory (str): The path to the directory where files are located.
    prefix (str): The prefix that the filenames should start with.

    Returns:
    list: A sorted list of filenames with the specified prefix.
    """
    # List all files in the specified directory
    files = os.listdir(directory)
    
    # Filter files with the given prefix
    matching_files = [file for file in files if file.startswith(prefix)]
    
    # Sort the filtered files
    matching_files.sort()
    
    return matching_files